"""
The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned.

The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

"""

def rgb(r, g, b):
    rgb_values = [r, g, b]
    letter_codes = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    output = ""

    # helper function to convert a digit
    def convert_digit(d):
        if d <= 9:
            return str(d)
        else:
            return letter_codes[d]

    for value in rgb_values:
        if value < 0:
            output += "00"
        elif value > 255:
            output += "FF"
        else:
            output += convert_digit(value // 16) + convert_digit(value % 16)

    return output


### TEST CODE ###

print(rgb(0, 0, 0)) # 000000
print(rgb(1, 2, 3)) # 010203
print(rgb(255, 255, 255)) # FFFFFF
print(rgb(254, 253, 252)) # FEFDFC
print(rgb(-20, 275, 125)) # 00FF7D
