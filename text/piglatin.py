#! /usr/bin/python2.7

import os
import re
import sys

# some static resources
vowels = set(('a','e','i','o','u','A','E','I','O','U'))
#vowel_re
consonant_re = re.compile(r'([bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]+)([a-zA-Z]*)(.*)?')

# input
original = sys.stdin.read()
# output
piglatin = []

# loop over the words and change them to pig latin
for word in original.split():
    # there are different rules if it starts with a vowel
    if word[0] in vowels:
        piglatin.append(word+'way')
    else:
        piglatin.append(consonant_re.sub(r'\2\1ay\3', word))

# output the translated text
sys.stdout.write(' '.join(piglatin))