#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-10
Purpose: Rock the Casbah
"""

import argparse
import sys
import io

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input File(s)',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])
    parser.add_argument('-c',
                        '--char',
                        action='store_true',
                        help='if included prints number of characters in the file',
                        default=False)
    parser.add_argument('-l',
                        '--linecount',
                        action='store_true',
                        help='if included prints number of lines in the file',
                        default=False)
    parser.add_argument('-w',
                        '--wordcount',
                        action='store_true',
                        help='if included prints number of words in the file',
                        default=False)
    parser.add_argument('--cat',
                        action='store_true',
                        help='prints content of the file',
                        default=False)
    parser.add_argument('--head',
                        action='store_true',
                        help='prints first line of the file',
                        default=False)
    parser.add_argument('--tail',
                        action='store_true',
                        help='prints last n of the file',
                        default=False)
    parser.add_argument('--tac')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
args=get_args()

total_lines, total_bytes, total_words = 0, 0, 0
for fh in args.file:
    num_lines, num_words, num_bytes = 0, 0, 0
    for line in fh:
        if args.linecount:
            num_lines += 1
        if args.char:
            num_bytes += len(line)
        if args.wordcount:
            num_words += len(line.split()) 
        total_lines += num_lines  
        total_bytes += num_bytes 
        total_words += num_words  
    print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')
if len(args.file) > 1:
    print(f'{total_lines:8}{total_words:8}{total_bytes:8} total')
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
