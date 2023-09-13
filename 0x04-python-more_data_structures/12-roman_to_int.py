#!/usr/bin/python3

def roman_to_int(roman_string):
    """Function to convert roman_string into integer

    Args:
        roman_string: The roman string to convert to integer

    Returns:
        It returns an intger, which is an equivalent of the roman string
    """
    if not (isinstance(roman_string, str)):
        return 0
    roman = dict(M=1000, C=100, D=500, X=10, L=50, V=5, I=1)
    total = roman[roman_string[-1]]
    near = total

    for numeral in roman_string[-2::-1]:
        if roman[numeral] < near:
            total = total - roman[numeral]
        else:
            total = total + roman[numeral]
        near = roman[numeral]
    return total
