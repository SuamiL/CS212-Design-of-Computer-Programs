# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 
from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn) #for n_ary_f->seq
    update_wrapper(_d, d) #for _d->n_ary
    return _d


@decorator
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        # your code here
        return x if not args else f(x, n_ary_f(*args))
    #DRY rule
    #update_wrapper(n_ary_f, f)
    return n_ary_f

## DECORATOR

@n_ary
def seq(x, y): return ('seq', x, y)
