#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-13
Purpose: Rock the Casbah
"""

import argparse
from pprint import pprint as pp

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)',
                        type=str)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    """args=get_args()
    letter_dict={}
    for line in args.file:
        letter_dict[line[0].lower()] = line.rstrip()

    for letter in args.letter:
        if letter in letter_dict:
            print(letter_dict[letter]) 
        else:
            print(f'I do not know {letter}')"""
    
    
    """word_count={}
    for line in args.file:
        for word in line.split():
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1
    for keys in word_count:
        print(keys,word_count[keys])"""
    
    args = get_args()
    lookup = {line[0].upper(): line.rstrip() for line in args.file}

    for letter in args.letter:
        print(lookup.get(letter.upper(), f'I do not know "{letter}".'))

# --------------------------------------------------
if __name__ == '__main__':
    main()
