#! /usr/bin/python2.7

# vowel count

import os
import sys

vowels = set(('a','e','i','o','u','A','E','I','O','U'))

data = sys.stdin.read()
count = 0L

if '--separate' in sys.argv:
    count = {'a': 0L,'e': 0L,'i': 0L,'o': 0L,'u': 0L}
    for char in data:
        if char in vowels:
            count[char.lower()] += 1
    
    for k in count.keys():
        print k,count[k]

else:    
    for char in data:
        if char in vowels:
            count += 1

    print count