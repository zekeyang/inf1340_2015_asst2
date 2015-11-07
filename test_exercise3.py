#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise3 import union, intersection, difference, MismatchedAttributesException


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

DOGS = [["Color", "Name", "Weight"],
            ["brown", "Barker", 32],
            ["white", "Gunner", 7],
            ["black", "Drake", 13]]

CATS = [["Color", "Name", "Weight"],
            ["black", "Shannon", 18],
            ["white", "Gunner", 7],
            ["black", "Drake", 13]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return sorted(t1) == sorted(t2)


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))

    result = [["Color", "Name", "Weight"],
                ["brown", "Barker", 32],
                ["white", "Gunner", 7],
                ["black", "Drake", 13],
                ["black", "Shannon", 18]]

    assert is_equal(result, union(DOGS, CATS))


def test_union_unexpected():
    """
    Test that raises MismatchedAttributesException
    This is when schema do not have same number of columns or columns do not have same names in the same order
    """
    try:
        union(GRADUATES, CATS)
    except MismatchedAttributesException:
        assert True


def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))

# Test pets operation to include a table with various schema

    result = [["Color", "Name", "Weight"],
            ["white", "Gunner", 7],
            ["black", "Drake", 13]]

    assert is_equal(result, intersection(DOGS, CATS))


def test_intersection_unexpected():
    """
    test that raises MismatchedAttributesException
    This is when schema do not have same number of columns or columns do not have same names in the same order
    """
    try:
        intersection(MANAGERS, DOGS)
    except MismatchedAttributesException:
        assert True



def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))

# Test pets operation to include a table with various schema

    result = [["Color", "Name", "Weight"],
            ["brown", "Barker", 32]]

    assert is_equal(result, difference(DOGS, CATS))


def test_difference_unexpected():
    """
    Test that raises MismatchedAttributesException
    This is when schema do not have same number of columns or columns do not have same names in the same order
    """
    try:
        difference(MANAGERS, CATS)
    except MismatchedAttributesException:
        assert True