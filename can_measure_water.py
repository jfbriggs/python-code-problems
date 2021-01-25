"""
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False


Constraints:

0 <= x <= 10^6
0 <= y <= 10^6
0 <= z <= 10^6
"""



def can_measure_water(x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """

    # define greatest common denominator func
    def gcd(x, y):
        if (x == 0) and (y != 0):
            return y
        elif (y == 0) and (x != 0):
            return x
        else:
            while x != y:
                if x > y:
                    x = x - y
                else:
                    y = y - x

        return x

    if x + y < z:
        return False

    if z % gcd(x, y) == 0:
        return True
    else:
        return False

## TEST CODE ##

print(can_measure_water(3, 5, 4)) # True
print(can_measure_water(2, 6, 5)) # False
print(can_measure_water(7, 10, 6)) # True