#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """

    counter = 0
    matching_position = -1
    sub_length = len(substring)
    start = int(start)
    end = int(end)
    end_index = (start + sub_length)
    while (end_index <= end) and (matching_position < 0):
        if input_string[(start + counter):(start + counter + sub_length)] == substring:
            matching_position = start + counter
        counter += 1
        end_index = start + counter + sub_length

    return matching_position


def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    return result

def main():
    input_string = raw_input("Enter your full string:")
    substring = raw_input("Enter your sub string:")
    start = raw_input("Enter starting position:")
    end = raw_input("Enter end position:")
    result = find(input_string, substring, start, end)
    print result

main()