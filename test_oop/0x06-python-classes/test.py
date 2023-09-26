#!/usr/bin/python3

module = __import__('0-square')
print(module.__doc__)
print(module.Square.__doc__)

Square = __import__('0-square').Square

print(".....")
my_square = Square()
print(type(my_square))
print(my_square.__dict__)

