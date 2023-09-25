#!/usr/bin/python3

def list_division(my_list1, my_list2, list_length):
    final_list = [0] * list_length
    max_len = max(len(my_list1), len(my_list2))

    for i in range(0, max_len):
        try:
            a = my_list1[i]
            b = my_list2[i]
            final_list[i] = a / b
        except TypeError:
            print("wrong type")
            final_list[i] = 0
        except ZeroDivisionError:
            print("division by 0")
            final_list[i] = 0
        except IndexError:
            print("Out of range")
            final_list[i] = 0
        finally:
            pass
    return final_list
