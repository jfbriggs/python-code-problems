"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

"""

def make_readable(seconds):
    hours = seconds // 3600
    min = seconds % 3600 // 60
    sec = seconds % 3600 % 60

    def double_digit_string(n):
        if n < 10:
            return "0" + str(n)
        else:
            return str(n)

    return "{}:{}:{}".format(double_digit_string(hours), double_digit_string(min), double_digit_string(sec))


## TEST CODE ##

print(make_readable(0)) # "00:00:00"
print(make_readable(5)) # "00:00:05"
print(make_readable(60)) # "00:01:00"
print(make_readable(86399)) # "23:59:59"
print(make_readable(359999)) # "99:59:59"
