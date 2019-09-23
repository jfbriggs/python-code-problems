"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

- A[i] == B[j];
- The line we draw does not intersect any other connecting (non-horizontal) line.
- Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:

Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2

"""

def max_uncrossed_lines(a, b):
    max_matches = 0
    for n in range(0, len(a)):
        i = n
        j = 0
        last_b_match = -1
        matches = 0

        while i < len(a):
            while j < len(b):
                if a[i] == b[j]:
                    matches += 1
                    last_b_match = j
                    i += 1
                    if i >= len(a):
                        break
                j += 1

            i += 1
            j = last_b_match + 1

        if matches > max_matches:
            max_matches = matches

    return max_matches


### TEST CODE ###

print(max_uncrossed_lines([2,5,1,2,5], [10,5,2,1,5,2])) # 3
print(max_uncrossed_lines([1,3,7,1,7,5], [1,9,2,5,1])) # 2
