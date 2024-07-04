import validators


def main():
    email=check(input("What is your email address? "))
    if email:
        print("Valid")
    else:
        print("Invalid")



def check(em):
    return validators.email(em)


if __name__=="__main__":
    main()