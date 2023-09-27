#!/usr/bin/python3


magic = __import__('103-magic_class').MagicClass

circle = magic(1)
print(circle.area())
print(circle.circumference())


circle = magic(7)
print(circle.area())
print(circle.circumference())
