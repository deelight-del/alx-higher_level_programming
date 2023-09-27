#!/usr/bin/python3

Square = __import__('6-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

mysquare = Square(3, (5, 2)) 
mysquare.my_print()
print("--")
