#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    if (lent == 0):
        alpha = None
    else:
        alpha = sentence[0]
    return lent, alpha
