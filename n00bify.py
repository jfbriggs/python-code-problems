"""
The internet is a very confounding place for some adults. Tom has just joined an online forum and is trying to fit in with all the teens and tweens.
It seems like they're speaking in another language! Help Tom fit in by translating his well-formatted English into n00b language.

The following rules should be observed:

- "to" and "too" should be replaced by the number 2, even if they are only part of a word (E.g. today = 2day)
- Likewise, "for" and "fore" should be replaced by the number 4
- Any remaining double o's should be replaced with zeros (E.g. noob = n00b)
- "be", "are", "you", "please", "people", "really", "have", and "know" should be changed to "b", "r", "u", "plz", "ppl", "rly", "haz", and "no" respectively (even if they are only part of the word)
- When replacing words, always maintain case of the first letter unless another rule forces the word to all caps.
- The letter "s" should always be replaced by a "z", maintaining case
- "LOL" must be added to the beginning of any input string starting with a "w" or "W"
- "OMG" must be added to the beginning (after LOL, if applicable,) of a string 32 characters* or longer
- All evenly numbered words** must be in ALL CAPS (Example: Cake is very delicious. becomes Cake IZ very DELICIOUZ)
- If the input string starts with "h" or "H", the entire output string should be in ALL CAPS
- Periods ( . ), commas ( , ), and apostrophes ( ' ) are to be removed
- ***A question mark ( ? ) should have more question marks added to it, equal to the number of words** in the sentence (Example: Are you a foo? has 4 words, so it would be converted to r U a F00????)
- ***Similarly, exclamation points ( ! ) should be replaced by a series of alternating exclamation points and the number 1, equal to the number of words** in the sentence (Example: You are a foo! becomes u R a F00!1!1)

* Characters should be counted AFTER: any word conversions, adding additional words, and removing punctuation. Excluding: All punctuation and any 1's added after exclamation marks ( ! ). Character count includes spaces.

** For the sake of this problem, "words" are simply a space-delimited substring, regardless of its characters. Since the output may have a different number of words than the input, words should be counted based on the output string.
- Example: whoa, you are my 123 <3 becomes LOL WHOA u R my 123 <3 = 7 words

*** The incoming string will be punctuated properly, so punctuation does not need to be validated.

"""

import re

def n00bify(text):
    word_replacements = {
        "be": "b",
        "are": "r",
        "you": "u",
        "please": "plz",
        "people": "ppl",
        "really": "rly",
        "have": "haz",
        "know": "no"
    }

    text_split = text.split(" ")
    word_count = len(text_split)

    for i in range(len(text_split)):
        current = text_split[i]
        capitalized = current == current.capitalize()
        current = current.lower()

        if current in word_replacements.keys():
            current = word_replacements[current]

        current = re.sub(r"too?", "2", current)
        current = re.sub(r"fore?", "4", current)
        current = re.sub("oo", "00", current)
        current = re.sub("s", "z", current)

        if capitalized:
            current = current.capitalize()

        text_split[i] = current

    text_joined = " ".join(text_split)
    text_joined = re.sub(r"[\.\,\']", "", text_joined)


    if text_joined[0].lower() == "w":
        text_joined = "LOL " + text_joined

    if text_joined[0].lower() == "h":
        text_joined = text_joined.upper()

    character_count = len(re.sub(r"[?!]", "", text_joined))

    if character_count >= 32:
        if text_joined[:3] == "LOL":
            text_joined = "LOL OMG" + text_joined[3:]
        else:
            text_joined = "OMG " + text_joined

    text_split = text_joined.split(" ")

    for i, word in enumerate(text_split):
        if i % 2 != 0:
            text_split[i] = word.upper()

    text_joined = " ".join(text_split)

    last_char = text_joined[-1]

    if last_char in ["!", "?"]:
        suffix = ""
        if text_joined[-1] == "?":
            suffix += "?" * (len(text_split))
        elif text_joined[-1] == "!":
            for i in range(len(text_split)):
                if i % 2 == 0:
                    suffix += "!"
                else:
                    suffix += "1"
        text_joined = text_joined[:-1] + suffix


    return text_joined


## TEST CODE ##

print(n00bify('Hi, how are you today?')) # 'HI HOW R U 2DAY?????'

print(n00bify('I think it would be nice if we could all get along.')) # 'OMG I think IT would B nice IF we COULD all GET along'

print(n00bify("Let's eat, Grandma!")) # 'Letz EAT Grandma!1!'
