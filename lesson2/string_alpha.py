import re
from functools import wraps


def fn_timer(function):

    @wraps(function)
    def function_timer(*args, **kwargs):
        import time
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print('%s costs %s (s)' % (function.func_name, t1 - t0))
        return result
    return function_timer


@fn_timer
def get_alpha_str1(s):
    result = ''.join([x for x in s if x.isalpha()])
    return result


@fn_timer
def get_alpha_str2(s):
    result = ''.join(re.findall(r'[A-Za-z]', s))
    return result


@fn_timer
def get_alpha_str3(s):
    result = re.sub(r'[^A-Za-z]', '', s)
    return result


@fn_timer
def get_alpha_str4(s):
    result = ''.join(re.split(r'[^A-Za-z]', s))
    return result


if __name__ == '__main__':

    with open('text.txt', 'r') as f:
        s = f.read()
    print(len(s))

    get_alpha_str1(s)
    get_alpha_str2(s)
    get_alpha_str3(s)
    get_alpha_str4(s)
