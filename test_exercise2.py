#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find

# Test cases should include a variety of initial characters.
# Include instances where substring is found and other where it is not found.

def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14

    assert find("You are powerful, young padowan", "padowan", 0, 31) == 24

    assert find("My name is Inigo", "Montoya", 0, 16) == -1


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"

    assert multi_find("Fa la la la la, la la la la", "a", 0, 20) == "1,4,7,10,13, 17, 20, 23, 26"

    assert multi_find("Do Re Mi Fa Sol La Ti", "deer", 0, 20) == -1 
