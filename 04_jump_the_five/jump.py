#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-09
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input Text')
    
    parser.add_argument('-w',
                        '--word',
                        action='store_true',
                        help='checks if user wants number as a word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}
    if args.word:
       jumper = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
              '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'} 
    
    for char in args.text:
        print(''.join([jumper.get(char,char)]),end='')
    print()

# --------------------------------------------------
if __name__ == '__main__':
    main()
