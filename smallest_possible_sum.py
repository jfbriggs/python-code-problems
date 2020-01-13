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

def solution(lst):
    # sort list
    lst = sorted(lst)
    # if first and last values in list are the same
    if lst[0] == lst[-1]:
        # return sum of the list
        return sum(lst)
    # for each element in the list
    for i in range(len(lst)):
        # calc modulo value of current val and first val
        mod_val = lst[i] % lst[0]
        # if that element % the first element == 0
        if mod_val == 0:
            # that element becomes the same as the first element
            lst[i] = lst[0]
        # otherwise
        else:
            # that element becomes the remainder of the modulo operation
            lst[i] = mod_val
    # re-run solution() on the modified list
    return solution(lst)


### TEST CODE ###
print(solution([6, 9, 21])) # 9
print(solution([11, 2, 19, 7])) # 4
print(solution([2, 2])) # 4
print(solution([7])) # 7
