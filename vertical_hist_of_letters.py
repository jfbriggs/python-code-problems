"""
You are given a string s. Your task is to count the number of each letter (A-Z), and make a vertical histogram as result.
Look at the following examples to understand the rules.

Example:

For s = "XXY YY ZZZ123ZZZ AAA BB C", the output should be:

          *
          *
          *
*       * *
* *   * * *
* * * * * *
A B C X Y Z

- Rules

- You just need to count the uppercase letters. Any other character will be ignored.
- Using * to represent the number of characters.
- The order of output is form A to Z. Characters that do not appear in the string are ignored.
- To beautify the histogram, there is a space between every pair of columns.
- There are no extra spaces at the end of each row. Also, use "\n" to separate rows.
"""
import string

def vertical_histogram_of(s):
    # establish counts for each letter
    uppers = string.ascii_uppercase
    letters = []
    counts = []
    for letter in uppers:
        letter_count = s.count(letter)
        if letter_count > 0:
            letters.append(letter)
            counts.append(letter_count)

    # return empty string if no count values
    if len(counts) == 0:
        return ""

    # create list of asterisk-rows
    highest_count = max(counts)
    hist_rows = []

    # iterate through range (backwards) representing # of rows
    for i in range(highest_count, 0, -1):
        # determine last index of column with matching count value for the row
        last_matching = 0
        for j, val in enumerate(counts):
            if val >= i:
                last_matching = j

        # generate row-string with * or space up to applicable index
        row = ""
        for k in range(last_matching + 1):
            if counts[k] >= i:
                row = row + "* "
            else:
                row = row + "  "

        # append row to rows list, excluding unnecessary space at end of row-string
        hist_rows.append(row[:-1])

    # combine row-strings by joining with newline character
    hist_string = "\n".join(hist_rows)

    # return final combined string that includes row of letters associated with columns
    return hist_string + "\n" + " ".join(letters)



## TEST CODE ##

print(vertical_histogram_of("XXY YY ZZZ123ZZZ AAA BB C"))

"""
          *
          *
          *
*       * *
* *   * * *
* * * * * *
A B C X Y Z
"""

print(vertical_histogram_of("AAABBC"))

"""
*
* *
* * *
A B C
"""

print(vertical_histogram_of("abc123")) # empty string
