#! /usr/bin/env python

from __future__ import print_function

# Author: Victor Terron (c) 2015
# Email: `echo vt2rron1iaa32s | tr 132 @.e`
# License: GNU GPLv3

""" How do you determine whether a string is a permutation of another? """

import unittest

def is_permutation(word, another):
    # First of all we need to remove all 
    # the white spaces of "word" and "another".
    word = word.replace(" ", "")
    another = another.replace(" ", "")

    # After that, we can start by counting 
    # the total number of characters 
    # that each of the words has.
    long_word = len(word)
    long_another = len(another)

    # Now we can compare the length of each word, 
    # if one of them has a different size we can 
    # confirm that it's not a permutation.
    if long_word != long_another:
        return False

    # Now we are going to order the word, in such a way that if we enter 
    # "hola" the final result will be "ahlo". 
    # This procedure will help us to compare later 
    # if they have the same words.
    sorted_word = sorted(word.lower())
    sorted_another = sorted(another.lower())


    # The last thing we have left is to put a "for" that looks 
    # at the two words letter by letter and see if they have the same letters.
    # If it doesn't exist, we know it's not a permutation
    for x in range(long_word):
        if (sorted_word[x] != sorted_another[x]):
            return False

    # If our two words have passed all our tests, we can say that it's a
    # permutation
    return True


class AllUniqueTests(unittest.TestCase):

  def test_all_unique(self):
    self.assertTrue (is_permutation("", ""))
    self.assertTrue (is_permutation("a", "a"))
    self.assertTrue (is_permutation("aab", "aba"))
    self.assertTrue (is_permutation("dog", "God"))
    self.assertTrue (is_permutation("Buckethead", "Death Cube K"))
    self.assertTrue (is_permutation("Quid est veritas", "Est vir qui adest"))
    self.assertFalse(is_permutation("draft", "soft"))
    self.assertFalse(is_permutation("master", "muster"))

if __name__ == "__main__":
    unittest.main()
