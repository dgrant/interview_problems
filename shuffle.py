#!/usr/bin/env python3

import random
def shuffle(deck):
    for i in range(len(deck)-1, 0, -1):
        source = random.randint(0, i-1)
#        print('source=', source)
        temp = deck[i]
        deck[i] = deck[source]
        deck[source] = temp

        
deck = []
for suit in ('H', 'C', 'D', 'S'):
    deck += [str(x) + suit for x in ['A'] + list(range(2, 11)) + ['J', 'Q', 'K']]
print(deck)
shuffle(deck)
print(deck)
