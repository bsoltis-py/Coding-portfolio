import tkinter as tk
from tkinter import messagebox
import random
import simpleaudio as sa

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("U.S. State Capitals Quiz")

        # Define questions and answers for U.S. states
        self.flashcards_data = """
        Alabama|Montgomery
        Alaska|Juneau
        Arizona|Phoenix
        Arkansas|Little Rock
        California|Sacramento
        Colorado|Denver
        Connecticut|Hartford
        Delaware|Dover
        Florida|Tallahassee
        Georgia|Atlanta
        Hawaii|Honolulu
        Idaho|Boise
        Illinois|Springfield
        Indiana|Indianapolis
        Iowa|Des Moines
        Kansas|Topeka
        Kentucky|Frankfort
        Louisiana|Baton Rouge
        Maine|Augusta
        Maryland|Annapolis
        Massachusetts|Boston
        Michigan|Lansing
        Minnesota|St. Paul
        Mississippi|Jackson
        Missouri|Jefferson City
        Montana|Helena
        Nebraska|Lincoln
        Nevada|Carson City
        New Hampshire|Concord
        New Jersey|Trenton
        New Mexico|Santa Fe
        New York|Albany
        North Carolina|Raleigh
        North Dakota|Bismarck
        Ohio|Columbus
        Oklahoma|Oklahoma City
        Oregon|Salem
        Pennsylvania|Harrisburg
        Rhode Island|Providence
        South Carolina|Columbia
        South Dakota|Pierre
        Tennessee|Nashville
        Texas|Austin
        Utah|Salt Lake City
        Vermont|Montpelier
        Virginia|Richmond
        Washington|Olympia
        West Virginia|Charleston
        Wisconsin|Madison
        Wyoming|Cheyenne
        """

        # Convert the string into a list of dictionaries
        self.flashcards = [self.parse_flashcard(qa) for qa in self.flashcards_data.strip().split("\n")]

        self.current_flashcard = None
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=400)
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 12), width=40)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit Answer", width=20, height=2, command=self.check_answer)
        self.submit_button.pack(pady=5)

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 12))
        self.score_label.pack(pady=10)

        # Initialize answer_buttons attribute as an empty list
        self.answer_buttons = []

        # Start the quiz with the first flashcard
        self.next_flashcard()

    def parse_flashcard(self, qa):
        parts = qa.split("|")
        if len(parts) == 2:
            return {"question": f"What is the capital of {parts[0].strip()}?", "answer": parts[1].strip()}
        else:
            raise ValueError(f"Invalid format for flashcard: {qa}")

    def next_flashcard(self):
        if len(self.flashcards) == 0:
            messagebox.showinfo("Congratulations!", "You've completed the quiz!")
            self.root.destroy()
            return

        self.current_flashcard = random.choice(self.flashcards)
        self.question_label.config(text=self.current_flashcard['question'])

        # Decide whether to use multiple-choice or fill-in option
        use_multiple_choice = random.choice([True, False])

        if use_multiple_choice:
            self.setup_multiple_choice()
        else:
            self.setup_fill_in()

    def setup_multiple_choice(self):
        for widget in self.answer_buttons + [self.answer_entry]:
            widget.pack_forget()  # Hide all widgets

        # Choose the correct answer index randomly
        correct_answer_index = random.randint(0, 3)

        # Choose three incorrect options from other flashcards
        incorrect_options = random.sample(self.get_all_answers_except_current(), 3)

        # Set the answer options on the buttons
        self.answer_buttons = []  # Clear the answer_buttons list
        for i in range(4):
            button = tk.Button(self.root, text="", width=20, height=2, command=lambda i=i: self.check_answer(i))
            self.answer_buttons.append(button)
            button.pack(pady=5)

            if i == correct_answer_index:
                button.config(text=self.current_flashcard["answer"], state=tk.NORMAL, bg="#4CAF50", fg="white")
            else:
                button.config(text=incorrect_options.pop(), state=tk.NORMAL, bg="#f44336", fg="white")

    def setup_fill_in(self):
        for widget in self.answer_buttons + [self.answer_entry]:
            widget.pack_forget()  # Hide all widgets

        self.answer_entry.pack(pady=10)
        self.answer_entry.config(state=tk.NORMAL)
        self.answer_entry.delete(0, tk.END)

    def check_answer(self, index=None):
        if index is not None:
            user_answer = self.answer_buttons[index]["text"].strip()
        else:
            user_answer = self.answer_entry.get().strip()

        correct_answer = self.current_flashcard["answer"].strip()

        # Perform a case-insensitive comparison
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.play_ding_sound()
            messagebox.showinfo("Correct!", "Great job! You got it right!")
            self.update_score()
            self.remove_current_flashcard()
            self.next_flashcard()
        else:
            messagebox.showerror("Incorrect", f"Oops! The correct answer is {correct_answer}. Try again!")

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def remove_current_flashcard(self):
        self.flashcards.remove(self.current_flashcard)

    def play_ding_sound(self):
        try:
            wave_obj = sa.WaveObject.from_wave_file("ding.wav")  # Replace "ding.wav" with your sound file name
            play_obj = wave_obj.play()
            play_obj.wait_done()
        except Exception as e:
            print(f"Error playing sound: {e}")

    def get_all_answers_except_current(self):
        return [flashcard["answer"] for flashcard in self.flashcards if flashcard != self.current_flashcard]

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

