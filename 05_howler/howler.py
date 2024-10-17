#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-10
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-case input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or a file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file name',
                        metavar='outfile',
                        type=str,
                        default='')

    parser.add_argument('-ee',
                        help='Lowercsae all characters in a file or string',
                        action='store_true',
                        default=False)
    
    args = parser.parse_args()
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
    args = get_args()
    fh_out = open(args.outfile, 'wt') if args.outfile else sys.stdout
    fh_out.write(args.text.lower() + '\n') if args.ee else fh_out.write(args.text.upper() + '\n')
    fh_out.close


""" args = get_args()
    pos_arg = args.text
    text = pos_arg
    if os.path.isfile(text):
        fh_in = open(text)
        if args.outfile != '':
            to_write = fh_in.read().upper()
            fh_out = open(f'{args.outfile}', 'wt')
            fh_out.write(to_write)
            fh_out.close()
        else:
            print(fh_in.read().upper(), end='')
    else:
        if args.outfile != '':
            to_write = text.upper()
            fh_out = open(f'{args.outfile}', 'wt')
            fh_out.write(to_write)
            fh_out.close()
        else:
            print(text.upper())"""

        
# --------------------------------------------------
if __name__ == '__main__':
    main()
