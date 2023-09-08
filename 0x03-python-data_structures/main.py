#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

my_list = [1, 2, 3, 4, 5]
idx = -3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

my_list = []
print("No list")
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
print("After no list")

my_list = [1, 2, 3, 4, 5]
print("Greater index")
idx = 10
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
