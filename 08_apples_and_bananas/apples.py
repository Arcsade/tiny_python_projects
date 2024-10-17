#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-14
Purpose: Rock the Casbah
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Text')

    parser.add_argument('-v',
                        '--vowel',
                        help='Vowel to replace with',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou')) 
    
    args=parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    new_text=[args.vowel if char in 'aeiou' else args.vowel.upper() if char in 'AEIOU' else char for
              char in args.text]
    print(''.join(new_text))
# --------------------------------------------------
if __name__ == '__main__':
    main()
