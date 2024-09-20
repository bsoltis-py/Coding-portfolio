Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

======================================================================= RESTART: /Users/bensoltis/Desktop/BenSoltisHandsOn4.py =======================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltisHandsOn4.py", line 31, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltisHandsOn4.py", line 7, in main
    food, name, place, animal, profession, things, clothing, verb, verb2 = getWords
TypeError: cannot unpack non-iterable function object

======================================================================= RESTART: /Users/bensoltis/Desktop/BenSoltisHandsOn4.py =======================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltisHandsOn4.py", line 31, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltisHandsOn4.py", line 6, in main
    story1 = getWords
UnboundLocalError: cannot access local variable 'getWords' where it is not associated with a value

======================================================================= RESTART: /Users/bensoltis/Desktop/BenSoltisHandsOn4.py =======================================================================
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltisHandsOn4.py", line 30, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltisHandsOn4.py", line 6, in main
    story1 = getWords = food, name, place, animal, profession, things, clothing, verb, verb2
NameError: name 'food' is not defined

======================================================================= RESTART: /Users/bensoltis/Desktop/BenSoltisHandsOn4.py =======================================================================
Enter a food: pizza
Enter a name: ben
Enter a place: NOVA
Enter a animal: dog
Enter a profession: professor
Enter a thing, plural: shoes
Enter a type of clothing: shirt
Enter a verb: run
Enter another verb: walk

======================================================================= RESTART: /Users/bensoltis/Desktop/BenSoltisHandsOn4.py =======================================================================
Enter a food: pizza
Enter a name: ben
Enter a place: nova
Enter a animal: dog
Enter a profession: professor
Enter a thing, plural: shoes
Enter a type of clothing: shirt
Enter a verb: run
Enter another verb: walk
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltisHandsOn4.py", line 33, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltisHandsOn4.py", line 7, in main
    madlib1(food, name, place)
  File "/Users/bensoltis/Desktop/BenSoltisHandsOn4.py", line 25, in madlib1
    print(f'"Say {food}!", the photographer said as the camera flashed! {name.capitilize()} and I had gone to {place.capitilize()} to get our photos taken on my birthday.')
AttributeError: 'str' object has no attribute 'capitilize'. Did you mean: 'capitalize'?

======================================================================= RESTART: /Users/bensoltis/Desktop/BenSoltisHandsOn4.py =======================================================================
Enter a food: pizza
Enter a name: ben
Enter a place: Nova
Enter a animal: dog
Enter a profession: doctor
Enter a thing, plural: shoes
Enter a type of clothing: shoe
Enter a verb: running
Enter another verb: walking
"Say pizza!", the photographer said as the camera flashed! Ben and I had gone to Nova to get our photos taken on my birthday.
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/BenSoltisHandsOn4.py", line 33, in <module>
    main()
  File "/Users/bensoltis/Desktop/BenSoltisHandsOn4.py", line 8, in main
    madlib2(animal, profession)
TypeError: madlib2() missing 1 required positional argument: 'place'
>>> 
======================================================================= RESTART: /Users/bensoltis/Desktop/BenSoltisHandsOn4.py =======================================================================
Enter a food: pizza
Enter a name: Ben
Enter a place: Nova
Enter a animal: Dog
Enter a profession: doctor
Enter a thing, plural: shoes
Enter a type of clothing: shirt
Enter a verb: running
Enter another verb: walking
"Say pizza!", the photographer said as the camera flashed! Ben and I had gone to Nova to get our photos taken on my birthday.
The first photo we really wanted was a picture of us dressed as DOG pretending to be a DOCTOR.
When we running the second photo, it was exactly what I wanted.  We both looked like shoes wearing shirt and WALKING!
>>> 
======================================================================= RESTART: /Users/bensoltis/Desktop/BenSoltisHandsOn4.py =======================================================================
Enter a food: hamburger
Enter a name: John
Enter a place: Chicago
Enter a animal: cat
Enter a profession: doctor
Enter a thing, plural: shoes
Enter a type of clothing: shirt
Enter a verb: ate
Enter another verb: walking
"Say hamburger!", the photographer said as the camera flashed! John and I had gone to Chicago to get our photos taken on my birthday.

The first photo we really wanted was a picture of us dressed as CAT pretending to be a DOCTOR.

When we ate the second photo, it was exactly what I wanted.  We both looked like shoes wearing shirt and WALKING!
>>> 
======================================================================= RESTART: /Users/bensoltis/Desktop/BenSoltisHandsOn4.py =======================================================================
Enter a food: pizza
Enter a name: ben
Enter a place: nova
Enter a animal: bird
Enter a profession: doctor
Enter a thing, plural: shoes
Enter a type of clothing: shirt
Enter a verb: ran
Enter another verb: walked

"Say pizza!", the photographer said as the camera flashed! Ben and I had gone to Nova to get our photos taken on my birthday.

The first photo we really wanted was a picture of us dressed as BIRD pretending to be a DOCTOR.

When we ran the second photo, it was exactly what I wanted. We both looked like shoes wearing shirt and WALKED!
>>> 
======================================================================= RESTART: /Users/bensoltis/Desktop/BenSoltisHandsOn4.py =======================================================================
Enter a food: cat
Enter a name: ben
Enter a place: ohio
Enter a animal: dogs
Enter a profession: doctor
Enter a thing, plural: shoes
Enter a type of clothing: pants
Enter a verb: look
Enter another verb: walked

"Say cat!", the photographer said as the camera flashed! Ben and I had gone to Ohio to get our photos taken on my birthday.

The first photo we really wanted was a picture of us dressed as DOGS pretending to be a DOCTOR.

When we look the second photo, it was exactly what I wanted. ßWe both looked like shoes wearing pants and WALKED!
