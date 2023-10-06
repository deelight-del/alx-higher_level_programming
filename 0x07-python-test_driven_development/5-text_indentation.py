#!/usr/bin/python3

"""This module contains the function definition
of the print text indentation.
"""


def text_indentation(text):
    """Function to indent a text when it encounters certain variables.

    Args:
        text: The text to indent appropriately.

    Return:
        None. prints indented text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    if text == "":
        return
    sentence_list = []
    prev_str_idx = 0
    for i, character in enumerate(text):
        if character == "." or character == "?" or character == ":":
            sentence_list.append(text[prev_str_idx:i+1])
            prev_str_idx = i + 1

    if i != prev_str_idx:
        sentence_list.append(text[prev_str_idx:])

    stripped_sentence_list = [substring.strip() for substring in sentence_list]
    text_print = stripped_sentence_list[0]
    if len(stripped_sentence_list) > 1:
        text_print = text_print + "\n\n" +\
                "\n\n".join(stripped_sentence_list[1:])
    print(text_print, end="")
