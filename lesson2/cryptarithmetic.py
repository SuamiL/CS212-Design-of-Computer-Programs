import itertools
import string
import re
import time


def solve(formula):
    """Given a formula lisk 'ODD + ODD = EVEN', fill in digits to solve it.
    Input formula is a sting; output is a digit-filled-in string or None."""
    for f in formula:
        if valid(f):
            return f


def fill_in(formula):
    """Generate all possible fillings-in of letters in formula with digits."""
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, digits)
        yield formula.translate(table)


def valid(f):
    """Formula f is valid if it has no numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and evals(f) is True
    except ArithmeticError:
        return False


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.E.g., 
    compile_word('YOU') => '(1*U+10*O+100*Y)' Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10**i, d)) for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result"
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def timedcalls(n, fn, *args):
    "Call function n times with args; return the min, avg, and max time"
    times = [timedcall(fn, *args)[0] for _ in range(n)]
    return min(times), avg(times), max(times)


# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))
# print(list(enumerate(seasons, start=1)))
# print(list(enumerate(seasons[::-1], start=1)))
help(timedcall)
