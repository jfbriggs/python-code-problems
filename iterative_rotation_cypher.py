"""
To complete the task, you will create an object with two methods, encode and decode.

Input:
The encode method will receive two arguments — a positive integer n and a string value.
The decode method will receive one argument — a string value.

Output:
Each method will return a string value.

How It Works:
Encoding and decoding are done by performing a series of character and substring rotations on a string input.

Encoding: The number of rotations is determined by the value of n. The sequence of rotations is applied in the following order:
 Step 1: remove all spaces in the string (but remember their positions)
 Step 2: shift the order of characters in the new string to the right by n characters
 Step 3: put the spaces back in their original positions
 Step 4: shift the characters of each substring (separated by one or more consecutive spaces) to the right by n
Repeat this process until it has been completed n times in total.
The value n is then prepended to the resulting string with a space.

Decoding: Decoding simply reverses the encoding process.
"""

def shift_right(s, n):
    for i in range(n):
        s = s[-1] + s[:-1]

    return s

def encode(n,strng):
    ## Step 1
    space_indices = [i for i, val in enumerate(strng) if val == ' '] # create list of indices of spaces in string
    strng = strng.replace(' ', '') # remove spaces

    ## Step 2
    strng = shift_right(strng, n)

    ## Step 3
    for idx in space_indices:
        substring = strng[:idx]
        strng = substring + ' ' + strng[idx:]

    



def decode(strng):
	#your code goes here. you can do it!
	pass


## TEST CODE

quote = 'If you wish to make an apple pie from scratch, you must first invent the universe.'
solution = '10 hu fmo a,ys vi utie mr snehn rni tvte .ysushou teI fwea pmapi apfrok rei tnocsclet'

encode(5, "Hey there buddy")
# encode(10, quote)
# print(encode(10, quote) == solution)
# print(decode(solution) == quote)
