import itertools
import string
import re


def faster_solve(formula):
    """Given a formula lisk 'ODD + ODD = EVEN', fill in digits to solve it.
    Input formula is a sting; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula. """
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass


def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. For example, 'YOU == ME**2' returns
    (lambda Y, M, E, U, O: (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO' """
    letters = ''.join(set(re.findall('[A-Z', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: return f
    return eval(f), letters


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.E.g.,
    compile_word('YOU') => '(1*U+10*O+100*Y)' Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10**i, d)) for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

#test enumerate
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))
# print(list(enumerate(seasons, start=1)))
# print(list(enumerate(seasons[::-1], start=1)))
