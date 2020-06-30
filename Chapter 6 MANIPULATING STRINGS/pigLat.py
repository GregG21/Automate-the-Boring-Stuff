print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
pigLatin = []
for word in message.split():
    prefixNonLatters = ""
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLatters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLatters)
        continue


    suffixNonLetters = ""
    while not  word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    prefixConstant = ""
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConstant += word[0]
        word = word[1:]

    if prefixConstant !="":
        word += prefixConstant + "ay"
    else:
        word += "yay"


    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    pigLatin.append(prefixNonLatters + word + suffixNonLetters)

print("".join(pigLatin))

