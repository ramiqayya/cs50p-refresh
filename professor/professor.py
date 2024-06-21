import random


def main():
    level = get_level()
    count = 0
    score = 10
    while True:
        trials = 3
        a, b = generate_integer(level)
        c = a + b
        while True:
            if trials == 0:
                print(f"{a} + {b} = {c}")
                score -= 1
                count += 1
                break
            try:
                ans = int(input(f"{a} + {b} = "))
                if ans == c:
                    count += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                trials -= 1
        if count == 10:
            print("Score=", score)
            break


def get_level():
    while True:
        try:
            le = int(input("Level: "))
            if 3 < le or le < 1:
                raise ValueError
            else:
                return le
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
    elif level == 2:
        x = random.randint(0, 100)
        y = random.randint(0, 100)
    elif level == 3:
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
    return x, y


if __name__ == "__main__":
    main()
