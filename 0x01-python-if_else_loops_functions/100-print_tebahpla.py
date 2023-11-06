iteration = 0
VAL = 122
def add_subtract(VAL):
    if iteration == 0:
        return VAL
    if iteration % 2 == 0:
        VAL += 31
    else:
        VAL -= 33
    return VAL




while iteration < 26:
    VAL = add_subtract(VAL)
    print(chr(VAL), end='')
    iteration += 1
