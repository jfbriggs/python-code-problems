"""
A format for expressing an ordered list of integers is to use a comma separated list of either:

- individual integers
- or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]) returns "-6,-3-1,3-5,7-11,14,15,17-20"

"""

def solution(args):
    result = ""
    curr_subrange_start = args[0]
    curr_subrange_end = args[0]

    def create_substring(start, end, is_last):
        output = ""

        if curr_subrange_end >= curr_subrange_start + 2: # if the current subrange contains at least 3 values
            output += str(start) + "-" + str(end)
        else: # if the current subrange is only 1 or 2 values
            if curr_subrange_start != curr_subrange_end:
                output += str(curr_subrange_start) + ","
            output += str(curr_subrange_end)

        if not is_last:
            output += ","

        return output

    for i in range(1, len(args)):
        if args[i] > curr_subrange_end + 1: # if the current value is more than 1 greater than the prior (meaning the current subrange is ending)
            result += create_substring(curr_subrange_start, curr_subrange_end, False)
            # reset subrange values to current value in loop
            curr_subrange_start = args[i]
            curr_subrange_end = args[i]
        else: # if the current value is just 1 greater than the prior value
            curr_subrange_end += 1

    result += create_substring(curr_subrange_start, curr_subrange_end, True)

    return result



## TEST CODE ##
print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])) # '-6,-3-1,3-5,7-11,14,15,17-20'
print(solution([-3,-2,-1,2,10,15,16,18,19,20])) # '-3--1,2,10,15,16,18-20'
