#!/usr/bin/env python3
"""
Author : arcsade <arcsade@localhost>
Date   : 2024-10-16
Purpose: Rock the Casbah
"""

import argparse
import os
import re
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    return args
 
#---------------------------------------------------

def fry(text):
    """
    ing_word = re.search('(.+)ing$', text)
    you = re.match('([Yy])ou$', text)
    your = re.match('([Yy])our$',text)
    if ing_word:
        prefix=ing_word.group(1)
        if re.search('[aeiouy]', prefix, re.IGNORECASE):
            return prefix + "in'"
    elif you:
        return you.group(1)+"'all"
    elif your:
        return your.group(1)+"'all's"
    return text"""

    if text.lower()=='you':
        return text[0]+"'all"
    elif text.lower()=='your':
        return text[0]+"'all's"
    elif text[:5].lower()=='think':
        return (('R' if text[0].isupper() else 'r')+'eckon'+(text[5:-1] + "'" if text[5:]=='ing' else text[5:]))
    elif text[-3:]=='ing':
        #if any(map(lambda c:c.lower() in 'aeiouy',text[:-3])):
        if [True for c in text[:-3] if c.lower() in 'aeiouy']:
            return text[:-1]+"'"
        else:
            return text
    return text
    """
    for word in text.split():
        if word[-3:] == 'ing' and [True for c in word[:-3] if c in 'aeiou']:
            text=text[:text.index(word)] + word[:-3] + "in'" + text[text.index(word)+len(word):]
        elif word[-4:-1] == 'ing' and [True for c in word[:-4] if c in 'aeiou']:
            text=text[:text.index(word)] + word[:-4] + "in'" + text[text.index(word)+len(word)-1:]
        elif word == 'You' or word == 'you':
            text=text[:text.index(word)] + "y'all" if word[0] == 'y' else "Y'all" + text[text.index(word)+len(word):]
    return text"""
#-----------------------------------------------------------------------------------
    # words = re.split(r'(\W+)',text)
    """new_words=''
    for word in words:
        if word[-3:] == 'ing' and [True for c in word[:-3] if c in 'aeiou']:
            new_words+=str(word[:-3]) + "in'"
        elif word.lower() == 'you':
            new_words+= word[0] + "'all""
        else:
            new_words+=word
    return new_words"""

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(''.join(map(fry,re.split(r'(\W+)',args.text))))
# --------------------------------------------------
if __name__ == '__main__':
    main()
