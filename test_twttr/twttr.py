def main():
    text= input("Input: ")

    # shorten(text)
    print(shorten(text))


def shorten(word):
    
    vowels=['a','e','o','u','i','A','E','O','U','I']
    new_text=''
    for i in range(len(word)):
        if word[i] not in vowels:
            new_text+=word[i]

    # print(f"{text[i]}",end='')
    

    return new_text
    


if __name__ == "__main__":
    main()