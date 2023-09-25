#!/usr/bin/python3

def list_division(my_list1, my_list2, list_length):
    final_list = [0] * list_length
    max_len = max(len(my_list1), len(my_list2))

    for i in range(0, list_length):
        try:
            a = my_list1[i]
            b = my_list2[i]
            c = a / b
        except TypeError:
            print("wrong type")
            c = 0
        except ZeroDivisionError:
            print("division by 0")
            c = 0
        except IndexError:
            print("out of range")
            c = 0
        finally:
            final_list[i] = c
    return final_list
