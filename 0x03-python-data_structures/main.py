#!/usr/bin/python3

multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
s = ""
length, first = multiple_returns(s)
print("Length: {:d} - First character: {}".format(length, first))

