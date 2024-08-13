from libraries.roman_numeral import RomanNumeral

saved_characters = 0
with open("data/0089_roman.txt") as f:
    for s in f:
        s = s.strip()
        number = RomanNumeral(s)
        correct = str(number)
        saved_characters += len(s) - len(correct)

print(saved_characters)
