#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

G1 = [["Number", "Surname", "Age"],
            [7274, "Robinson", 37],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38],
            [2323, "Davidson", 86]]
G2 = [["Number", "Surname", "Age"],
            [8888, "McKay", 80],
            [7432, "O'Malley", 39],
            [5959, "McCowan", 89],
            [3434, "Henderson", 85],
            [2323, "Davidson", 86]]


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    combine_table = []
    if table1[0] == table2[0]:
        combine_table.append(table1[0])
        combine_table.extend(table1[1:])
        combine_table.extend(table2[1:])
        union_table = list(remove_duplicates(combine_table))
        return union_table
    else:
        try:
            raise MismatchedAttributesException("The database schemas do not match")
        except MismatchedAttributesException, e:
            print e


def intersection(table1, table2):
    """
    Describe your function

    """
    # combine_table = []
    # if table1[0] == table2[0]:
    #     combine_table.append(table1[0])
    #     if len(table1) >= len(table2):
    #         loop_num_greater = len(table1)
    #         loop_num_less = len(table2)
    #         big_table = list(table1)
    #         small_table = list(table2)
    #     else:
    #         loop_num_greater = len(table2)
    #         loop_num_less = len(table1)
    #         big_table = list(table2)
    #         small_table = list(table1)
    #
    #     for counter1 in range(1, loop_num_less):
    #         for counter2 in range(1, loop_num_greater):
    #             if small_table[counter1] == big_table[counter2]:
    #                 combine_table.append(big_table[counter2])
    #     intersection_table = list(remove_duplicates(combine_table))
    #     return intersection_table
    # else:
    #     return combine_table

    intersection_table = []
    if table1[0] == table2[0]:
        intersection_table.append(table1[0])
        loop_num = len(table1)
        for counter in range(1, loop_num):
            if any(table1[counter] == item for item in table2):
                intersection_table.append(table1[counter])
        return intersection_table
    else:
        try:
            raise MismatchedAttributesException("The database schemas do not match")
        except MismatchedAttributesException, e:
            print e


def difference(table1, table2):
    """
    Describe your function

    """
    difference_table = []
    if table1[0] == table2[0]:
        difference_table.append(table1[0])
        loop_num = len(table1)
        for counter in range(1, loop_num):
            if not any(table1[counter] == item for item in table2):
                difference_table.append(table1[counter])
        return difference_table
    else:
        try:
            raise MismatchedAttributesException("The database schemas do not match")
        except MismatchedAttributesException, e:
            print e


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass


print union(G1, G2)