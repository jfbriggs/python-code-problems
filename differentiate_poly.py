"""
Create a function that differentiates a polynomial for a given value of x.

Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate the equation as an integer.

Assumptions:
There will be a coefficient near each x, unless the coefficient equals 1 or -1.
There will be an exponent near each x, unless the exponent equals 0 or 1.
All exponents will be greater than or equal to zero.

Examples:

differentiate("12x+2", 3)      ==>   returns 12
differentiate("x^2+3x+2", 3)   ==>   returns 9
"""

def differentiate(equation, point):
    return


### TEST CODE ###

print(differentiate("12x+2", 3)) # 12
print(differentiate("x^2-x", 3)) # 5
print(differentiate("-5x^2+10x+4", 3)) # -20
