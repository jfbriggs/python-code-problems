"""
Given an array X of positive integers, its elements are to be transformed by running the following operation on them as many times as required:

if X[i] > X[j] then X[i] = X[i] - X[j]

When no more transformations are possible, return its sum ("smallest possible sum").

Example
solution([6, 9, 21]) #-> 9

Solution steps:
[6, 9, 12] #-> X[2] = 21 - 9
[6, 9, 6] #-> X[2] = 12 - 6
[6, 3, 6] #-> X[1] = 9 - 6
[6, 3, 3] #-> X[2] = 6 - 3
[3, 3, 3] #-> X[1] = 6 - 3

"""
from math import gcd
from functools import reduce

def solution(lst):
    return len(lst) * reduce(gcd, lst)


### TEST CODE ###
print(solution([6, 9, 21])) # 9
print(solution([11, 2, 19, 7])) # 4
print(solution([2, 2])) # 4
print(solution([7])) # 7
