#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-18
Purpose: Rock the Casbah
"""

import argparse
import csv
import csvkit
import tabulate as t
import pprint as pp
import io
import re
import random
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file for exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args=parser.parse_args()

    if args.num < 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args

#---------------------------------------------------
def read_csv(file):
    """Read the csv input"""
    with file:
        if file.name[-3:] in ('csv','tab'):
            delim={'csv':',','tab':'\t'}
            reader = csv.DictReader(file,delimiter = delim[file.name[-3:]] )
            records=[]
            for rec in reader:
                name,reps = rec.get('exercise'),rec.get('reps')
                if name and reps:
                    match = re.match(r'(\d+)-(\d+)', reps)
                    if match:
                        low, high = map(int,match.groups())       # match=re.match('(\d+)-(\d+)',reps) 
                        records.append((name,low,high))           # match.group(1),match.group(2)
        else:
            sys.exit('Invalid delimiter')
    return(records)
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    exercises=read_csv(args.file)
    if not exercises:
        sys.exit(f'No usable data in --file "{args.file.name}"')
    num_exercises = len(exercises)
    if args.num > num_exercises:
        sys.exit(f'--num "{args.num}" > exercises "{num_exercises}"')
    wod=[]
    for exercise,low,high in random.sample(exercises,args.num):
        wod.append((exercise,int((random.randint(low,high))/2) if args.easy else (random.randint(low,high))))
    print(t.tabulate(wod, headers=('Exercise', 'Reps'), tablefmt='grid',showindex=True))


#--------------------------------------------------
def test_read_csv():
    """Test read_csv"""
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
