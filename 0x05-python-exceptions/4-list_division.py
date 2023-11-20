#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            result_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("Division by 0")
            result_list.append(0)
        except IndexError:
            print("Out of range")
            result_list.append(0)
        except TypeError:
            print("Wrong type")
            result_list.append(0)
    return result_list
