def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>6 or len(s)<2:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    for i in range(len(s)-1):
        if s[i].isdigit() and (s[i+1]).isalpha():
            return False
    for j in range(len(s)-1):
        if s[j].isalpha() and (s[j+1])=='0':
            return False
    for k in s:
        if not k.isalpha():
            if not k.isdigit():
              return False
    return True


if __name__=="__main__":
    main()