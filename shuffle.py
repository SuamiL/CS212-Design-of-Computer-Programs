import random
from math import factorial
from collections import defaultdict

#random card
# def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
#     "Shuffle the deck and deal out numhands n-card hands"
#     random.shuffle(deck)
#     return [deck[n*i : n*(i+1)] for i in range(numhands)]

def shuffle1(deck):
    "bad shuffle"
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)

def swap(deck, i, j):
    "swap elements i and j of a collection"
    #print('swap', i, j)
    deck[i], deck[j] = deck[j], deck[i]

def shuffle(deck):
    "good shuffle"
    N = len(deck)
    for i in range(N-1):
        swap(deck, i, random.randrange(i, N))

#test_shuffler
def test_shuffler(shuffler, deck='abcd', n=10000):
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1
    e = n*1./factorial(len(deck))
    ok = all((0.9 <= counts[item]/e <= 1.1)
             for item in counts)

    name = shuffler.__name__
    print('%s(%s) %s' % (name, deck, ('ok' if ok else '***BAD***')))
    print('   ',)
    for item, count in sorted(counts.items()):
        print("%s:%4.1f" % (item, count*100./n),)
    print()

def test_shuffles(shufflers = [shuffle, shuffle1], decks = ['abc', 'ab']):
    for deck in decks:
        print()
        for f in shufflers:
            test_shuffler(f, deck)

def shuffle2(deck):
    "O(N^2)  correct"
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = True
        swap(deck, i, j)

def shuffle3(deck):
    "O(N) incorrect"
    N = len(deck)
    for i in range(N):
        swap(deck, i ,random.randrange(N))

test_shuffles([shuffle, shuffle1, shuffle2, shuffle3])







