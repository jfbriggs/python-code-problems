"""
Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero.
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Examples:

RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000

"""

class RomanNumerals:
    def __init__(self):
        self.chars = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        self.nums = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }


    def to_roman(n):
        # create inner helper function to convert each digit
        def convert_num(n, place):
            chars = {
                'hundreds': ['C', 'D', 'M'],
                'tens': ['X', 'L', 'C'],
                'ones': ['I', 'V', 'X']
            }

            result = ''

            if (n >= 1) and (n <= 3):
                for i in range(n):
                    result += chars[place][0]
            elif n == 4:
                result += chars[place][0] + chars[place][1]
            elif (n >= 5) and (n <= 8):
                result += chars[place][1]
                for i in range(n - 5):
                    result += chars[place][0]
            elif n == 9:
                result += chars[place][0] + chars[place][2]

            return result

        # create initial result string
        result = ''

        # convert thousands place
        for i in range(n // 1000):
            result += 'M'

        # convert hundreds place
        result += convert_num((n % 1000) // 100, 'hundreds')

        # convert tens place
        result += convert_num(n % 1000 % 100 // 10, 'tens')

        # convert ones place
        result += convert_num(n % 1000 % 100 % 10, 'ones')

        print(result)


    def from_roman(rn):
        pass


## TEST CODE ##

RomanNumerals.to_roman(1000) # 'M'
RomanNumerals.to_roman(1990) # 'MCMXC'
#
# RomanNumerals.from_roman('XXI') # 21
# RomanNumerals.from_roman('MMVIII') # 2008

RomanNumerals.to_roman(2156)
