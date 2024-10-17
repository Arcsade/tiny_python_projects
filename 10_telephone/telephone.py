#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-15
Purpose: Rock the Casbah
"""

import argparse
import os
import random
import string
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)
    
    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)
    
    parser.add_argument('-o',
                        '--output',
                        metavar='output',
                        help ='Output file name',
                        default=sys.stdout)
    
    parser.add_argument('-co',
                        '--charsonly',
                        action='store_true',
                        help='If enabled only characters are included',
                        default=False)
    
    parser.add_argument('-w',
                        '--words',
                        action='store_true',
                        help='If enabled randomly mutates words instead of the entire string',
                        default=False)
    
    args=parser.parse_args()

    if args.mutations>1.0 or args.mutations<0.0:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1!')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    return args
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    """
    args = get_args()
    random.seed(args.seed)
    num_mutations = round(len(args.text)*args.mutations)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation)) 
    new_text=''
    #for char in args.text:
    #   new_text+= random.choice(alpha) if random.random() <= args.mutations else char
    indexes = random.sample(range(len(args.text)),num_mutations)
    for i in range(len(args.text)):
        if i in indexes:
            new_text+= random.choice(alpha.replace(args.text[i],''))
        else:
            new_text+=args.text[i]
        
    print(f'You said: "{args.text}"')
    print(f'I heard : "{new_text}"')
    """
    args = get_args()
    text = args.text
    random.seed(args.seed)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    if args.charsonly:
        alpha=''.join(sorted(string.ascii_letters))
    len_text = len(text)
    num_mutations = round(args.mutations * len_text)
    new_text = text

    if args.words:
        word_mutation = round(len(args.text.split())*args.mutations)
        words = random.sample(args.text.split(),word_mutation)
        for word in words:
            new_word = ''
            for i in range(len(word)):
                new_char = random.choice(alpha.replace(word[i], ''))
                new_word+= new_char 
            new_text = new_text[:args.text.index(word)] + new_word + new_text[args.text.index(word) + len(word):]  
    else:
        for i in random.sample(range(len_text), num_mutations):
            new_char = random.choice(alpha.replace(new_text[i], ''))
            new_text = new_text[:i] + new_char + new_text[i + 1:]

        
    if args.output != sys.stdout:
        open(args.output,'wt').write(f'{new_text}\n') 
    else:
        print(f'You said: "{text}"\nI heard : "{new_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
