"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

"""

def is_letter(char):
    if (ord(char) >= 65) and (ord(char) <= 122):
        return True
    else:
        return False

def pig_it(text):
    split_text = text.split(" ")
    new_words = []

    for word in split_text:
        if len(word) > 1:
            first_char = ""
            last_char = ""
            if not is_letter(word[0]):
                first_char = word[0]
                word = word[1:]
            if not is_letter(word[-1]):
                last_char = word[-1]
                word = word[:-1]

            word = first_char + word[1:] + word[0] + "ay" + last_char

        else:
            if is_letter(word):
                word = word + "ay"

        new_words.append(word)

    return " ".join(new_words)




## TEST CODE ##

print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('Hello world !'))     # elloHay orldway !
print(pig_it("Hey buddy, how are you?")) # eyHay uddybay, owhay reaay ouyay?
