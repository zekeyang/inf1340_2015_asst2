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
    A game to modify a word with two rules:
    a) If a word begins with a vowel, append "yay" to then end of the word.
    b) If the word begins with a consonant, remove all the consonants from the beginning up to
    :param word: input word
    :return result: the modified word
    :raises:

    """

    if word.isalpha():  # to be removed
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
    else:
        result = ""
        return result


# def main():
#     user_input = raw_input("Input a word:")
#     output = pig_latinify(user_input)
#     print output
#
# main()
