# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!
import math

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    longest, res = 0, (0, 0)
    if text == '': return res
    for i in range(1, 2*len(text)-2, 1):
        i = i/2
        if isinstance(i, int):
            start, end =  i-1, i+1  
        else:
            start, end = math.floor(i), math.ceil(i)
        length, ran = find_subpalin(text, start, end)
        if length > longest:
            longest = length
            res = ran
    res = (res[0], res[1]+1)
    return res


def find_subpalin(text, start, end):
    while start >= 0 and end <= (len(text)-1) and (text[start].lower() == text[end].lower()):
        start = start - 1
        end = end + 1
    return end-start+2, (start+1, end-1)

    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print(test())

#teacher's solution
# def longest_subpalindrome_slice(text):
#     if text == '': return (0,0)
#     def length(slice): a, b = slice; return b-a
#     candidates = [grow(text, start, end)
#                   for start in range(len(text))
#                   for end in (start, start+1)]
#     return max(candidates, key=length)

# def grow(text, start, end):
#     while (start > 0 and end < len(text)
#            and text[start-1].upper() == text[end].upper()):
#         start -= 1; end += 1
#     return (start, end)