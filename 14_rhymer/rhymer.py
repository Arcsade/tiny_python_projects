#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-16
Purpose: Rock the Casbah
"""

import argparse
import re
import string as s
import sys
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Making rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    parser.add_argument('-o',
                        '--outfile',
                        type=argparse.FileType('a'),
                        default = sys.stdout,
                        help='Output filename')

    args = parser.parse_args()

    if os.path.isfile(args.word):
        args.word=open(args.word).read().rstrip()

    return args

#---------------------------------------------------
def stemmer(word):
    """Return leading consonants(if any) and 'stem' of the word"""
    word=word.lower()
    vowels='aeiou'
    consonants=''.join([c for c in s.ascii_lowercase if c not in vowels])
    pattern = (
            '([' + consonants + ']+)?' # capture one or more, optional
            '([' + vowels     + '])'   # capture at least one vowel
            '(.*)'                     # capture zero or more of anything
            )
    match = re.match(pattern, word)
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1, p2 + p3)
    else:
        return (word, '')

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    """args = get_args()

    rhyword=''

    for char in args.word:
        if char.lower() in 'aeiou':
            rhyword = args.word[args.word.index(char):]
            break
        else:
            rhyword = ''
    if rhyword == '':
        print(f'Cannot rhyme "{args.word}"')
    else:    
        prefixes = list('bcdfghjklmnpqrstvwxyz') + ('bl br ch cl cr dr fl fr gl gr pl pr sc '
                    'sh sk sl sm sn sp st sw th tr tw thw wh wr '
                    'sch scr shr sph spl spr squ str thr').split()
        prefixes.sort()

        for prefix in prefixes:
            if prefix+rhyword.lower()!=args.word.lower():
                print(prefix+rhyword.lower())"""
    
    args = get_args()
    prefixes = list('bcdfghjklmnpqrstvwxyz') + ('bl br ch cl cr dr fl fr gl gr pl pr sc '
                'sh sk sl sm sn sp st sw th tr tw thw wh wr '
                'sch scr shr sph spl spr squ str thr').split()
    for word in args.word.split():
        start, rest = stemmer(word)
        if args.outfile == sys.stdout:
            if rest:
                print('\n'.join(sorted([p + rest for p in prefixes if p != start])))
            else:
                print(f'Cannot rhyme "{word}"')
        else:
            args.outfile.write('\n'.join(sorted([p + rest for p in prefixes if p != start]))+'\n' 
                                if rest else f'Cannot rhyme "{word}"'+'\n')

    
# --------------------------------------------------
if __name__ == '__main__':
    main()

#---------------------------------------------------
def test_stemmer():
    """ Test stemmer """
    assert stemmer('') == ('','')
    assert stemmer('cake') == ('c','ake')
    assert stemmer('chair') == ('ch','air')
    assert stemmer('APPLE') == ('','apple')
    assert stemmer('123') == ('123','')