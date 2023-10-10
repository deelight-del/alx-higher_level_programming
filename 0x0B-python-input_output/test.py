#!/usr/bin/python3

next_triangle = __import__('12-pascal_triangle').next_triangle
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle
print(next_triangle([1, 1]))
print(next_triangle([1, 2, 1]))

print(pascal_triangle(1))
print(pascal_triangle(2))
print(pascal_triangle(3))
print(pascal_triangle(4))
print(pascal_triangle(5))
print(pascal_triangle(6))
print(pascal_triangle(7))
