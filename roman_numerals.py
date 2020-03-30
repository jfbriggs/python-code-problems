"""
Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero.
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Examples:

RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000\

"""

class RomanNumerals():
    def __init__(self):
        pass

    def to_roman(self, n):
        pass

    def from_roman(self, rn):
        pass


## TEST CODE ##

RomanNumerals.to_roman(1000) # 'M'
RomanNumerals.to_roman(1990) # 'MCMXC'

RomanNumerals.from_roman('XXI') # 21
RomanNumerals.from_roman('MMVIII') # 2008
