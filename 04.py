#! /usr/bin/env python

from __future__ import print_function

# Author: Victor Terron (c) 2015
# Email: `echo vt2rron1iaa32s | tr 132 @.e`
# License: GNU GPLv3

""" How do you count the number of digits of an integer? """

def ndigits(number):
    str_num = str(number)
    if str_num[0] == '-':
        num = len(str(str_num))-1
    else:
        num = len(str(str_num))
    return num

if __name__ == "__main__":

    print(ndigits(3))   # 1
    print(ndigits(-5))  # 1
    print(ndigits(27))  # 2
    print(ndigits(495)) # 3
