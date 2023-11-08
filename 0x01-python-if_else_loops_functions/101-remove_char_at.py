def remove_char_at(str, n):
    strlen = len(str)
    i = 0
    while i < strlen:
        if i == n:
            i += 1
            continue
        elif n > strlen or n < 0:
            print(str, end='')
            break
        print(str[i], end='')
        i += 1
    print('')
