#!/usr/bin/python3

def magic_calculation(a, b):
    """Function to interpret python bytecode

    Args:
        a: first operand
        b: second operand

    Return:
        It returns an integer.
    """

    result = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception('Too far')
            else:
                result += (b ** a) / i
        except Exception as e:
            result = a + b
            break
    return result
