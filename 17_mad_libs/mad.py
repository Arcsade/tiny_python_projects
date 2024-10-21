#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-17
Purpose: Rock the Casbah
"""

import argparse
import re
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)
    
    parser.add_argument('-i',
                        '--inputs',
                        nargs='*',
                        type=str,
                        help='Inputs for testing',
                        metavar='Inputs(for testing)',
                        default=None)

    return parser.parse_args()

#--------------------------------------------------
def libs(file,inputs):
    text=file.read().rstrip()
    matches=re.findall('(<([^<>]+)>)', text)
    if matches==[]:
        sys.exit(f'"{file.name}" has no placeholders.')
    for placeholder,words in matches:
        if inputs:
            text=re.sub(placeholder,inputs.pop(0),text,count=1,flags=0)
        else:
            in_word=input(f'Give me {'an' if words[0] in 'aeiou' else 'a'} {words} ')
            text=re.sub(placeholder,in_word,text,count=1,flags=0)
    return text
#---------------------------------------------------
"""def html_tags(file):
    pass
    text=file.read().rstrip()
    matches=re.findall('(<([^<>]+)>)', text)
    matches+=re.findall('(</([^<>]+)>)', text)
    for placeholder,words in matches:
        print(placeholder,words)"""
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(libs(args.file,args.inputs))
    #html_tags(args.file)
        
# --------------------------------------------------
if __name__ == '__main__':
    main()
                    