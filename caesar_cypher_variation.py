"""
The action of a Caesar cipher is to replace each plaintext letter with a different one a fixed number of places up or down the alphabet.

This program performs a variation of the Caesar shift. The shift increases by 1 for each character (on each iteration).

If the shift is initially 1, the first character of the message to be encoded will be shifted by 1, the second character will be shifted by 2, etc...

Coding: Parameters and return of function "movingShift"
param s: a string to be coded

param shift: an integer giving the initial shift

The function "movingShift" first codes the entire string and then returns an array of strings containing the coded string in 5 parts (five parts because, to avoid more risks, the coded message will be given to five runners, one piece for each runner).

If possible the message will be equally divided by message length between the five runners. If this is not possible, parts 1 to 5 will have subsequently non-increasing lengths, such that parts 1 to 4 are at least as long as when evenly divided, but at most 1 longer. If the last part is the empty string this empty string must be shown in the resulting array.

For example, if the coded message has a length of 17 the five parts will have lengths of 4, 4, 4, 4, 1. The parts 1, 2, 3, 4 are evenly split and the last part of length 1 is shorter. If the length is 16 the parts will be of lengths 4, 4, 4, 4, 0. Parts 1, 2, 3, 4 are evenly split and the fifth runner will stay at home since his part is the empty string. If the length is 11, equal parts would be of length 2.2, hence parts will be of lengths 3, 3, 3, 2, 0.

You will also implement a "demovingShift" function with two parameters

Decoding: parameters and return of function "demovingShift"
1) an array of strings: s (possibly resulting from "movingShift", with 5 strings)

2) an int shift

"demovingShift" returns a string.

Example:
u = "I should have known that you would have a perfect answer for me!!!"

movingShift(u, 1) returns :

v = ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]

(quotes added in order to see the strings and the spaces, your program won't write these quotes, see Example Test Cases)

and demovingShift(v, 1) returns u. #Ref:

Caesar Cipher : http://en.wikipedia.org/wiki/Caesar_cipher

"""
from math import ceil

def moving_shift(s, shift):
    shifted_string = ""

    # shift forward helper function
    def shift_forward(c, n):
        char_value = ord(c)
        if (char_value >= 65) and (char_value <= 90): # capital letter
            char_value = char_value + (n % 26)
            if char_value > 90:
                char_value = char_value - 90 + 64
        elif (char_value >= 97) and (char_value <= 122): # lowercase
            char_value = char_value + (n % 26)
            if char_value > 122:
                char_value = char_value - 122 + 96

        return chr(char_value)

    # shift all characters in string
    for char in s:
        shifted_string += shift_forward(char, shift)
        shift += 1

    # generate list of split values
    splits = []
    length = len(s)

    if length % 5 != 0:
        split_value = ceil(length / 5)
    else:
        split_value = int(length / 5)

    while len(splits) < 5:
        if length >= split_value:
            splits.append(split_value)
            length -= split_value
        else:
            splits.append(length)
            length -= length

    # generate split string
    result = []
    for val in splits:
        result.append(shifted_string[:val])
        shifted_string = shifted_string[val:]

    # return split string
    return result


def demoving_shift(s, shift):
    # join string
    s = "".join(s)

    #shift back helper function
    def shift_backward(c, n):
        char_value = ord(c)
        if (char_value >= 65) and (char_value <= 90): # capital letter
            char_value = char_value - (n % 26)
            if char_value < 65:
                char_value = 90 - (64 - char_value)
        elif (char_value >= 97) and (char_value <= 122): # lowercase
            char_value = char_value - (n % 26)
            if char_value < 97:
                char_value = 122 - (96 - char_value)

        return chr(char_value)

    # iterate through string, shifting each character back
    result = ""
    for c in s:
        result += shift_backward(c, shift)
        shift += 1

    return result


## TEST CODE ##

print(moving_shift("I should have known that you would have a perfect answer for me!!!", 1)) # ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]
print(demoving_shift(["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"], 1)) # "I should have known that you would have a perfect answer for me!!!"
