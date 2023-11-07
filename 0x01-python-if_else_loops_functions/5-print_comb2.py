#!/usr/bin/python3
for i in range(100):
    if i in range(0, 99):
        print(f'{i:02}', end=", ")
    else:
        print(i)

