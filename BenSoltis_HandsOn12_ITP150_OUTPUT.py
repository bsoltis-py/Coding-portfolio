Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Enter 1 for Rock, 2 for Paper, 3 for Scissors: 
Enter the number: 1
Enter the number: 2
Enter the number: 3
main()
Enter 1 for Rock, 2 for Paper, 3 for Scissors: 
Enter the number: 4
Enter the number: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Enter 1 for Rock, 2 for Paper, 3 for Scissors: 
Enter the number: a
Not an integer, please try again.
Enter the number: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Enter 1 for Rock, 2 for Paper, 3 for Scissors: 
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 26, in main
    usrInpt.append(int(input("Enter the number: ")))
AttributeError: 'str' object has no attribute 'append'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 36, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 31, in main
    except usrInpt not in ["1","2","3"]:
TypeError: catching classes that do not inherit from BaseException is not allowed

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 44, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 20, in main
    RPS_outcomes = [[Win, Lose, Tie],[Win, Win, Tie],[Win, Tie, Win],[],[],[],[],[]]
NameError: name 'Win' is not defined. Did you mean: 'bin'?

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 48, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 35, in main
    usrInpt.append(int(input("Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: ")))
NameError: name 'usrInpt' is not defined

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 50, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 37, in main
    usr_choice.append = int(input("Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: "))
NameError: name 'usr_choice' is not defined

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 50, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 42, in main
    if not usr_choice.isdigit() or usr_choice not in ["0","1", "2"]:
AttributeError: 'int' object has no attribute 'isdigit'

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 50, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 42, in main
    if not usr_choice.isdigit(0,2) or usr_choice not in ["0","1", "2"]:
AttributeError: 'int' object has no attribute 'isdigit'

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Not a valid integer, try again
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
Not a valid integer, try again
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 3
Not a valid integer, try again
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 4
Not a valid integer, try again
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 50, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 42, in main
    if not usr_choice.isdigit in ["0","1","2"]:
AttributeError: 'int' object has no attribute 'isdigit'


=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 50, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 42, in main
    if not usr_choice.isdigit in ["0","1","2"]:
AttributeError: 'int' object has no attribute 'isdigit'

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 50, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 42, in main
    if not usr_choice.isdigit() in ["0","1","2"]:
AttributeError: 'int' object has no attribute 'isdigit'

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
Not a valid integer, try again
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Not a valid integer, try again
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 71, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 33, in main
    while comp_win < 2 and usr_win < 2:
NameError: name 'usr_win' is not defined. Did you mean: 'user_win'?

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 3
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 3
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 3
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 3
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 71, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 45, in main
    while comp_choice not in ["1","2","3"]:
NameError: name 'comp_choice' is not defined. Did you mean: 'user_choice'?

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Invalid integer. Please enter 1, 2, or 3. Try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
Invalid integer. Please enter 1, 2, or 3. Try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 3
Invalid integer. Please enter 1, 2, or 3. Try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 4
Invalid integer. Please enter 1, 2, or 3. Try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 5
Invalid integer. Please enter 1, 2, or 3. Try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 60
Invalid integer. Please enter 1, 2, or 3. Try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
Invalid integer. Please enter 1, 2, or 3. Try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
Invalid integer. Please enter 1, 2, or 3. Try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: `
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 71, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 47, in main
    user_choice = int(input("Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: "))
ValueError: invalid literal for int() with base 10: '`'

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 4
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 5
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 6
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 3
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
Invalid integer. Please enter 1, 2, or 3. Try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 61, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 36, in main
    while True and user_choice in ["1","2","3"]:
UnboundLocalError: cannot access local variable 'user_choice' where it is not associated with a value

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Not a vailid integer, please try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Not a vailid integer, please try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 3
Not a vailid integer, please try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: e
Not an integer or vaild integer, please try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: e
Not a integer, please try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 7
Not a vailid integer, please try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 66, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 19, in main
    RPS_outcomes = [[Win, Lose, Tie],[Win, Tie, Win],[Win, Tie, Lose],[Win, Lose, Lose],[Lose, Tie, Win],[Lose, Win, Tie],[Lose, Tie, Tie],[]]
NameError: name 'Win' is not defined. Did you mean: 'bin'?

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 3
Not a vailid integer, please try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
User chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: e
Not an integer, please try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 0
User chose 0
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose 1
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
User chose 2
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 3
Not a vailid integer, please try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose 1
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
User chose 2
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 0
User chose 0
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose 1
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose 1
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose 1
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose 1
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose 1
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose 1
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose 1
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose 1
Computer chose 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 90, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 28, in main
    comp_win, user_win, tie_win = play_cntr(RPS_outcomes)
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 71, in play_cntr
    if comp_choice == "Win":
NameError: name 'comp_choice' is not defined

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 90, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 28, in main
    comp_win, user_win, tie_win = play_cntr(RPS_outcomes)
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 71, in play_cntr
    if comp_choice == "Win":
NameError: name 'comp_choice' is not defined

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 85, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 19, in main
    RPS_outcomes = [[Tie, Win, Lose],[Win, Tie, Lose],[Lose, Win, Tie]]
NameError: name 'Tie' is not defined

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 85, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 28, in main
    comp_win, user_win, tie_win = play_cntr(RPS_outcomes)
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 62, in play_cntr
    result = RPS_outcomes[user_choice][comp_choice]
NameError: name 'user_choice' is not defined

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 85, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 28, in main
    comp_win, user_win, tie_win = play_cntr(RPS_outcomes)
TypeError: play_cntr() missing 2 required positional arguments: 'comp_choice' and 'RPS_outcomes'

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 80, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 28, in main
    comp_win, user_win, tie_win = play_cntr(RPS_outcomes)
TypeError: play_cntr() missing 2 required positional arguments: 'comp_choice' and 'RPS_outcomes'

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 80, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 28, in main
    comp_win, user_win, tie_win = play_cntr(RPS_outcomes)
TypeError: play_cntr() missing 2 required positional arguments: 'comp_choice' and 'RPS_outcomes'

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 80, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 28, in main
    comp_win, user_win, tie_win = play_cntr(user_choice, comp_choice, RPS_outcomes)
UnboundLocalError: cannot access local variable 'user_choice' where it is not associated with a value

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 83, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 28, in main
    comp_win, user_win, tie_win = play_cntr(user_choice, comp_choice, RPS_outcomes)
UnboundLocalError: cannot access local variable 'user_choice' where it is not associated with a value

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Paper
Its a tie
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 82, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 47, in main
    comp_win, user_win, tie_win = play_cntr(user_choice, comp_choice, RPS_outcomes)
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 78, in play_cntr
    tie_win = tie_win + 1
UnboundLocalError: cannot access local variable 'tie_win' where it is not associated with a value

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Scissors
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 81, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 46, in main
    comp_win, user_win, tie_win = play_cntr(user_choice, comp_choice, RPS_outcomes)
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 79, in play_cntr
    return comp_win, user_win, tie_win
UnboundLocalError: cannot access local variable 'comp_win' where it is not associated with a value

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Paper
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 81, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py", line 46, in main
    comp_win, user_win, tie_win = play_cntr(user_choice, comp_choice, RPS_outcomes)
TypeError: play_cntr() missing 3 required positional arguments: 'comp_win', 'user_win', and 'tie_win'

=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Paper
Its a tie
User score: 0, Computer Score: 0, Ties: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Scissors
User score: 0, Computer Score: 0, Ties: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
User chose Scissors
Computer chose Rock
User score: 0, Computer Score: 0, Ties: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 3
Not a vailid integer, please try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Paper
Its a tie
User score: 0, Computer Score: 0, Ties: 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 0
User chose Rock
Computer chose Scissors
User score: 0, Computer Score: 0, Ties: 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Paper
Its a tie
User score: 0, Computer Score: 0, Ties: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Rock
You win!
User score: 1, Computer Score: 0, Ties: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
User chose Scissors
Computer chose Paper
You win!
User score: 2, Computer Score: 0, Ties: 1
User wins!
Goodbye!
main()
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Paper
Its a tie

User score: 0, Computer Score: 0, Ties: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
User chose Scissors
Computer chose Scissors
Its a tie

User score: 0, Computer Score: 0, Ties: 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 0
User chose Rock
Computer chose Paper
You win!

User score: 1, Computer Score: 0, Ties: 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
User chose Scissors
Computer chose Scissors
Its a tie

User score: 1, Computer Score: 0, Ties: 3
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Rock
You win!

User score: 2, Computer Score: 0, Ties: 3
User wins!
Goodbye!
main()
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 0
User chose Rock
Computer chose Paper
You win!

User score: 1, Computer Score: 0, Ties: 0
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Scissors

User score: 1, Computer Score: 0, Ties: 0
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
User chose Scissors
Computer chose Scissors
Its a tie

User score: 1, Computer Score: 0, Ties: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Rock
You win!

User score: 2, Computer Score: 0, Ties: 1
User wins!
Goodbye!
main()
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: e
Not an integer, please try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 4
Not a vailid integer, please try again.
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Rock
You win!

User score: 1, Computer Score: 0, Ties: 0
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
User chose Scissors
Computer chose Paper
You win!

User score: 2, Computer Score: 0, Ties: 0
User wins!
Goodbye!
main()
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
User chose Scissors
Computer chose Paper
You win!

User score: 1, Computer Score: 0, Ties: 0
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Scissors

User score: 1, Computer Score: 0, Ties: 0
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
User chose Scissors
Computer chose Scissors
Its a tie

User score: 1, Computer Score: 0, Ties: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 0
User chose Rock
Computer chose Rock
Its a tie

User score: 1, Computer Score: 0, Ties: 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Paper
Its a tie

User score: 1, Computer Score: 0, Ties: 3
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Scissors

User score: 1, Computer Score: 0, Ties: 3
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Paper
Its a tie

User score: 1, Computer Score: 0, Ties: 4
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Rock
You win!

User score: 2, Computer Score: 0, Ties: 4
User wins!
Goodbye!
>>> 
=================================================================== RESTART: /Users/bensoltis/Desktop/BenSoltis_HandsOn12_ITP150.py ==================================================================
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Rock
You win!

User score: 1, Computer Score: 0, Ties: 0
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 0
User chose Rock
Computer chose Rock
Its a tie

User score: 1, Computer Score: 0, Ties: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 2
User chose Scissors
Computer chose Paper
You win!

User score: 2, Computer Score: 0, Ties: 1
User wins!
Goodbye!
>>> main()
Lets play Rock, Paper, Scissors
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Paper
Its a tie

User score: 0, Computer Score: 0, Ties: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Scissors
The computer wins!

User score: 0, Computer Score: 1, Ties: 1
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Paper
Its a tie

User score: 0, Computer Score: 1, Ties: 2
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Paper
Its a tie

User score: 0, Computer Score: 1, Ties: 3
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 1
User chose Paper
Computer chose Paper
Its a tie

User score: 0, Computer Score: 1, Ties: 4
Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: 0
User chose Rock
Computer chose Scissors
The computer wins!

User score: 0, Computer Score: 2, Ties: 4
Computer wins!
Goodbye!
