#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-15
Purpose: Rock the Casbah
"""

import argparse
import os
import random

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)
    
    parser.add_argument('-t',
                        '--transform',
                        action='store_true',
                        help='Trasforms ASCII characters',
                        default=False)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text=open(args.text).read().rstrip()

    return args

#---------------------------------------------------
def choose(char):
    return random.choice([char.lower(), char.upper()])

#----------------------------------------------------
def transform(char):
    t_dict={'A':'4','B':'|3','C':'(','D':'|)','E':'3','F':'|=','G':'(-','H':'|-|','I':'1','J':'_|',
            'K':'|<','L':'|_','M':'|\/|','N':'|\|','O':'0','P':'|`','Q':'(`)','R':'|7','S':'5','T':'+',
            'U':'|_|','V':'\/','W':'\/\/','X':'><','Y':'/','Z':'7_'}
    
    return(t_dict.get(char.upper(),char))

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    print(''.join(map(choose, args.text)))

    if args.transform:
        print(''.join(map(transform,args.text)))


# --------------------------------------------------
if __name__ == '__main__':
    main()

#---------------------------------------------------
def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)