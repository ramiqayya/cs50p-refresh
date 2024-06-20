from random import randint

while True:
    try:
        level=int(input("Level: "))
        if level>0:
            break
    except ValueError:
        pass

number=randint(0,level)

while True:
    try:
        guess=int(input("Guess:"))
        if guess>number:
            print("Too large!")
        elif guess<number:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
