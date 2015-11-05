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
    Letter by letter comparisons to find any match substring inside of a string. Only one index/position is
    returned even if multiple matchings exist

    :param input_string: the complete string user input
    :param substring: the substring user input for comparison
    :param start: the start position for comparison
    :param end: the end position (end-1) for comparison
    :return matching_position: -1 by default if nothing is found. If anything found, return the lowest index
                                where the substring is found.
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
    Letter by letter comparisons to find any match substring inside of a string. All index/positions are
    returned

    :param input_string: the complete string user input
    :param substring: the substring user input for comparison
    :param start: the start position for comparison
    :param end: the end position (end-1) for comparison
    :return matching_position: -1 by default if nothing is found. If anything found, return the lowest index
                                where the substring is found.
    """

    counter = 0
    matching_position = [-1]
    sub_length = len(substring)
    start = int(start)
    end = int(end)
    end_index = (start + sub_length)
    while end_index <= end:
        if input_string[(start + counter):(start + counter + sub_length)] == substring:
            matching_position.append(start + counter)
        counter += 1
        end_index = start + counter + sub_length

    # if anything matching, remove the -1 value in the list
    if len(matching_position) > 1:
        del matching_position[0]

    # convert a list to a string
    string_holder = (",".join(str(s) for s in matching_position))
    return string_holder
