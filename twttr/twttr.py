text= input("Input: ")
vowels=['a','e','o','u','i','A','E','O','U','I']
new_text=''
for i in range(len(text)):
    if text[i] not in vowels:
        new_text+=text[i]

    # print(f"{text[i]}",end='')
    

print(f'Output: {new_text}')