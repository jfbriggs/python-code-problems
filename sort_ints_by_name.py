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
    # int-string mappings
    ones = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    teens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }

    tens = {
        2: "twenty",
        3: "thirty",
        4: "fourty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }

    if len(arr) == 1:
        return arr

    # helper func to convert int to its name string
    def convert_int(num):
        
        name = ""
        if num < 10:
            name = ones[num]
        elif num < 20:
            name = teens[num]
        else:
            if num > 99:
                name = name + ones[num // 100] + " hundred"
                num = num % 100
            name = name + " " + tens[num // 10]
            num = num % 10
            if num > 0:
                name = name + " " + ones[num]

        return name.strip()

    # if arr is NOT empty
    if len(arr) > 1:
        names_and_nums = sorted([(convert_int(num), num) for num in arr])
        return [val[1] for val in names_and_nums]


### TEST CODE ###

print(sort_by_name([8, 8, 9, 9, 10, 10])) # [8, 8, 9, 9, 10, 10]

print(sort_by_name([1, 2, 3, 4])) # [4, 1, 3, 2]

print(sort_by_name([9, 99, 999])) # [9, 999, 99]
