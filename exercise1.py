#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author1__ = 'Zixiao Yang'
__email1__ = "zeke.yang@mail.utoronto.ca"
__author2__ = 'Hana Nagel'
__email2__ = ""  #Hana, please put your email here, thanks.


def pig_latinify(word):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """

    while not word.isalpha():
        word = raw_input("Input your word again:")
    word_length = len(word)
    word = word.lower()
    # making sure the word starts with a vowel
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        word += "yay"
    # if a word is not starting with a vowel, then it must start with a consonant
    else:
        for counter in range(word_length):
            # put each leading consonant to the end of the word
            if not (word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u"):
                leading_char = word[0]
                word = word.replace(word[0], "", 1)
                word += leading_char
                counter += 1
        word += "ay"
    result = word
    return result


def main():
    user_input = raw_input("Input a word:")
    output = pig_latinify(user_input)
    print output

main()
