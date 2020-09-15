"""
Sort integers by name.

Input
Range is 0-999.

There may be duplicates.
The array may be empty.

Example:

Input: [1, 2, 3, 4]
Equivalent names: "one", "two", "three", "four"
Sorted by name: "four", "one", "three", "two"
Output: [4, 1, 3, 2]

Notes:

Don't pack words together:
e.g. 99 may be "ninety nine" or "ninety-nine"; but not "ninetynine"
e.g 101 may be "one hundred one" or "one hundred and one"; but not "onehundredone"

Don't fret about formatting rules, because if rules are consistently applied it has no effect anyway:
e.g. "one hundred one", "one hundred two"; is same order as "one hundred and one", "one hundred and two"
e.g. "ninety eight", "ninety nine"; is same order as "ninety-eight", "ninety-nine"

"""

def sort_by_name(arr):
    return # sorted array


### TEST CODE ###

print(sort_by_name([8, 8, 9, 9, 10, 10])) # [8, 8, 9, 9, 10, 10]

print(sort_by_name([1, 2, 3, 4])) # [4, 1, 3, 2]

print(sort_by_name([9, 99, 999])) # [9, 999, 99]
