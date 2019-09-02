"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
Input: 2
Output: [0, 1, 1]
"""

def countBits(num):
    result = []

    for i in range(num + 1):
        binary = bin(i)[2:]
        result.append(binary.count('1'))

    return result

## TEST CODE ##
print(countBits(2))
