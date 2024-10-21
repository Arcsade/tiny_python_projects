#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-18
Purpose: Rock the Casbah
"""

import argparse
import os
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='Text',
                        help='Input text or a file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args
#---------------------------------------------------
def word2num(word):
    """Sum the ordinal values of all the characters"""
    return str(sum(map(ord, re.sub('[^A-Za-z0-9]', '', word))))

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        print(' '.join(map(word2num, line.split())))

# --------------------------------------------------
if __name__ == '__main__':
    main()
sum