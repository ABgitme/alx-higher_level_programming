def uppercase(str):
    for i, char in enumerate(str):
        if (ord(char) not in range(65, 91)) and (ord(char) in range(97, 123)):
            print(chr(ord(char) - 32), end='')
        else:
            print(str[i], end='')
    print()




uppercase('stop THIs 98')
