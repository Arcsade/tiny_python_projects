#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-18
Purpose: Rock the Casbah
"""

import argparse
import random
import re
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default = 3)
    
    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default = 4)
    
    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default = 3)
    
    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length',
                        metavar='maximun',
                        type=int,
                        default = 6)
    
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default = None)
    
    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true',
                        default=False)

    args = parser.parse_args()

    if args.max_word_len<args.min_word_len:
        parser.error(f'--max_word_len "{args.max_word_len}" can\'t be lesser than --min_word_len "{args.min_word_len}"')
    if args.num<1:
        parser.error(f'--num "{args.num}" can\'t be less than 1')
    if args.num_words<1:
        parser.error(f'--num "{args.num_words}" can\'t be less than 1')
    if not args.min_word_len>1:
        parser.error(f'Invalid --min_word_len value "{args.min_word_len}"')
    if not args.max_word_len>1:
        parser.error(f'invalid --max_word_len value "{args.max_word_len}"')
    return args
#---------------------------------------------------
def clean(word):
    #re.sub('[^a-z]','',word)
    #''.join(filter(lambda x:x in string.ascii_lowercase,word))
    return ''.join([char for char in word if char in string.ascii_lowercase])  

#---------------------------------------------------
def ransom(char):
    return random.choice([char.lower(), char.upper()])
#---------------------------------------------------
def l33t(text):
    dict_l33t={'a':'@','A':'4','O':'0','t':'+','E':'3','I':'1','s':'5'}
    list_l33t=[]
    for i in range(len(text)):
            list_l33t.append(dict_l33t.get(ransom(text[i]),ransom(text[i])))
    list_l33t.append(random.choice(string.punctuation))
    return ''.join(list_l33t)
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    words=set()

    def word_len(word):
        return args.min_word_len<len(word)<args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len,map(clean,line.lower().split())):
                words.add(word.title())

    words=sorted(words)

    for _ in range(args.num):
        passwords=''.join(random.sample(words,args.num_words))
        if args.l33t:
            print(l33t(passwords))
        else:
            print(passwords)
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
