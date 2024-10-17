#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=0)
    
    args=parser.parse_args()

    if args.num<1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args

#---------------------------------------------------
def verse(bottle):
    """Sing a bottle"""
    return'\n'.join([
                    f"{bottle} {'bottles' if bottle>1 else 'bottle'} of beer on the wall,", 
                    f"{bottle} {'bottles' if bottle>1 else 'bottle'} of beer,",
                    f"Take one down, pass it around,",
                    f"{bottle-1 if bottle-1>0 else 'No more'} {'bottles' if bottle-1!=1 else 'bottle'} of beer on the wall!"])
    

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))

# --------------------------------------------------

def test_verse():
    """Test verse"""
    last_verse = verse(1)
    assert last_verse == '\n'.join([
    '1 bottle of beer on the wall,', '1 bottle of beer,',
    'Take one down, pass it around,',
    'No more bottles of beer on the wall!'
    ])
    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
    '2 bottles of beer on the wall,', '2 bottles of beer,',
    'Take one down, pass it around,', '1 bottle of beer on the wall!'])

#-----------------------------------------------------

if __name__ == '__main__':
    main()
