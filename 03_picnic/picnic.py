#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-09
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items',
                        )
    parser.add_argument('-noo',
                        '--nooxford',
                        action='store_true',
                        help="Removes the comma between last 'and' and item before it",
                        )  
    parser.add_argument('-sep',
                        '--userseparator',
                        type=str,
                        metavar='str',
                        default=',',
                        help="User defined separator",
                        )
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    separator=args.userseparator

    if args.sorted:
        items.sort()
    bringing = ''
    if len(items) == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = ' and '.join(items)
    elif len(items)>2 and args.nooxford:
        items[-1] = ' and ' + items[-1]
        bringing = (f'{separator} ').join(items[:-1]) + ''.join(items[-1])
    else:
        items[-1] = 'and ' + items[-1]
        bringing = (f'{separator} ').join(items)

    print(f'You are bringing {bringing}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
