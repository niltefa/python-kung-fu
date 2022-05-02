#! /usr/bin/env python

from __future__ import print_function

# Author: Victor Terron (c) 2015
# Email: `echo vt2rron1iaa32s | tr 132 @.e`
# License: GNU GPLv3

""" Write a function that returns whether a string has all unique characters.
For extra points, do it without using any additional data structure (such as
lists or dictionaries). You can use any function in the standard library. """

import unittest

def all_unique(word):
    
    # First of all it is necessary to put all the words 
    # in lower case. Since A!=a, and precisely we want A=a.
    word = word.lower()

    # If there is only one character we know that it will be unique.
    if len(word)==1:
      return True
    
    # Here what I do is take the first character and compare it with all the others, 
    # then I take the second character and I compare it with the others... If at some 
    # point there are two the same, it means that not all the characters are different.
    for x in range(len(word)):
      for y in range(x + 1, len(word)):
        if word[x] == word[y]:
          return False
    
    return True

class AllUniqueTests(unittest.TestCase):

  def test_all_unique(self):

    self.assertTrue (all_unique(""))
    self.assertTrue (all_unique("a"))
    self.assertTrue (all_unique("B"))
    self.assertTrue (all_unique("abcde"))
    self.assertTrue (all_unique("aBcDe"))
    self.assertFalse(all_unique("aa"))    # Two a's
    self.assertFalse(all_unique("bB"))    # Two b's (in different cases)
    self.assertFalse(all_unique("abCdc")) # Two c's

if __name__ == "__main__":
    unittest.main()
