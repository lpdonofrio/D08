#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
def print_hist_old(h):
    for c in h:
        print(c, h[c])

def print_hist_new(h):
    for c in sorted(h):
        print(c, h[c])

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
pledge_histogram = {}


def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram_new(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1
    return dictionary


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    with open("pledge.txt", "r") as honor_code:
        text = honor_code.read()
        pledge_list = text.split()
    return pledge_list

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a ABOVE  ###########################
###############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    print_hist_new(histogram_new((get_pledge_list())))

if __name__ == '__main__':
    main()
