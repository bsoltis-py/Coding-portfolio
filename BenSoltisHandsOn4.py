#Ben Soltis
#ITP 150 Hands on 4
#Prof McNally

def main():
    food, name, place, animal, profession, things, clothing, verb, verb2 = getWords()
    madlib1(food, name, place)
    madlib2(animal, profession)
    madlib3(verb, things, clothing, verb2)

    
def getWords():
    food = str(input("Enter a food: "))
    name = str(input("Enter a name: "))
    place = str(input("Enter a place: "))
    animal = str(input("Enter a animal: "))
    profession = str(input("Enter a profession: "))
    things = str(input("Enter a thing, plural: "))
    clothing = str(input("Enter a type of clothing: "))
    verb = str(input("Enter a verb: "))
    verb2 = str(input("Enter another verb: "))
    return food, name, place, animal, profession, things, clothing, verb, verb2

def madlib1(food, name, place):
    print()
    print(f'"Say {food}!", the photographer said as the camera flashed! {name.capitalize()} and I had gone to {place.capitalize()} to get our photos taken on my birthday.')
    print()

def madlib2(animal, profession):
    print(f'The first photo we really wanted was a picture of us dressed as {animal.upper()} pretending to be a {profession.upper()}.')
    print()

def madlib3(verb, things, clothing, verb2):
    print(f'When we {verb} the second photo, it was exactly what I wanted. We both looked like {things.lower()} wearing {clothing.lower()} and {verb2.swapcase()}!')

main()
