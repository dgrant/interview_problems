#!/usr/bin/env python
import sys

def getrank(s):
    chars_left = [c for c in s]
    rank = 1
    for i, c in enumerate(s):
        print('===================')
        print('i=', i, 'c=', c)
        num_less_than = len(set([x for x in chars_left[i:] if ord(x) < ord(c)]))
        print('num_less_than=', num_less_than)
        rank += num_less_than * fac(len(s)-i-1)
        print('rank=', rank)
    return rank


def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fac(n-1)

s = sys.argv[1]
num_dupes = len(s) - len(set([c for c in s]))
print(getrank(s))
