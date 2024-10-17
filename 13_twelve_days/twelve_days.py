#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-15
Purpose: Rock the Casbah
"""

import argparse
import sys
import emoji
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days',
                        metavar='days',
                        type=int,
                        default=12)
    
    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        help='Outfile',
                        default=sys.stdout)
    
    args = parser.parse_args()

    if args.num < 1 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')
    
    return args

#---------------------------------------------------
"""
def days(num):
    #Create a verse

    t_dict={1:'partridge in a pear tree.',2:'Two turtle doves',3:'Three French hens',4:'Four calling birds',
            5:'Five gold rings',6:'Six geese a laying',7:'Seven :bird:s a swimming',8:'Eight maids a milking',
            9:'Nine ladies dancing',10:'Ten lords a leaping',11:'Eleven pipers piping',12:'Twelve drummers drumming'}

    d_dict={1:'first',2:'second',3:'third',4:'fourth',5:'fifth',6:'sixth',7:'seventh',8:'eighth',
            9:'ninth',10:'tenth',11:'eleventh',12:'twelfth'}
    

    new_text='\n'.join([f'On the {d_dict[num]} day of Christmas,',
                        f'My true love gave to me,'])
    
    i=num
    while i>0 and num!=1:
        if i!=1:
            new_text+=''.join(f'\n{emoji.emojize(t_dict[i])},')
        else:
            new_text+=''.join(f'\nAnd a {emoji.emojize(t_dict[i])}')
        i-=1
    if num==1:
        new_text+=''.join(f'\nA {emoji.emojize(t_dict[i])}')


    return new_text
"""
def verse(day):
    """Create a verse"""

    ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ]

    gifts = [
        'A partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,',
    ]

    lines = [
        f'On the {ordinal[day - 1]} day of Christmas,',
        'My true love gave to me,'
    ]

    lines.extend(reversed(gifts[:day]))

    if day > 1:
        lines[-1] = 'And ' + lines[-1].lower()

    return '\n'.join(lines)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    """if args.outfile!=sys.stdout:
        args.outfile.write('\n\n'.join(map(days,range(1,args.num+1))))
    else:
        print('\n\n'.join(map(days,range(1,args.num+1))))"""
    verses = map(verse, range(1, args.num + 1))
    print('\n\n'.join(verses), file=args.outfile)
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
