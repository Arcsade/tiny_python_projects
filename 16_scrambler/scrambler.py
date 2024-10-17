#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-17
Purpose: Rock the Casbah
"""

import argparse
import re
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of the words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')


    parser.add_argument('-s',
                        '--seed',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=None)
    
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

#---------------------------------------------------
def scramble(word):
    if len(word)>3 and re.match(r'\w+', word):
        scram_list=list(word[1:-1])
        random.shuffle(scram_list)
        word=word[0] +''.join(scram_list) + word[-1]
        #word=word[0] +''.join(sorted(scram_list)) + word[-1] middle part sorted
        #---------------------------------------------------------
        #new_word=''                                        
        #for i in range(len(word)-1,-1,-1):          reverse the word or 
        # return ''.join(reversed(word))
        #    new_word+=word[i]
        #word=new_word
    return word
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    print(''.join(map(scramble,splitter.split(args.text))))

# --------------------------------------------------
if __name__ == '__main__':
    main()
