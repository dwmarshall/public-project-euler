class RomanNumeral:

    def __init__(self, *args):
        if type(args[0]) is int:
            self.number = args[0]
        else:
            self.number = self._roman_to_int(args[0])

    def __str__(self):
        return self._int_to_roman(self.number)

    @staticmethod
    def _int_to_roman(number: int) -> str:
        ones_digits = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens_digits = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        huns_digits = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

        pieces = []

        number, ones = divmod(number, 10)
        pieces.append(ones_digits[ones])
        number, tens = divmod(number, 10)
        pieces.append(tens_digits[tens])
        number, huns = divmod(number, 10)
        pieces.append(huns_digits[huns])
        pieces.append("M" * number)
        return "".join(reversed(pieces))

    @staticmethod
    def _roman_to_int(roman: str) -> int:
        roman_digits = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        digits = []
        i = 0
        while i < len(roman):
            if roman[i] == "I":
                if i + 1 < len(roman) and roman[i + 1] in "VX":
                    digits.append(roman[i : i + 2])
                    i += 2
                else:
                    digits.append(roman[i])
                    i += 1
            elif roman[i] == "X":
                if i + 1 < len(roman) and roman[i + 1] in "LC":
                    digits.append(roman[i : i + 2])
                    i += 2
                else:
                    digits.append(roman[i])
                    i += 1
            elif roman[i] == "C":
                if i + 1 < len(roman) and roman[i + 1] in "DM":
                    digits.append(roman[i : i + 2])
                    i += 2
                else:
                    digits.append(roman[i])
                    i += 1
            else:
                digits.append(roman[i])
                i += 1

        number = 0
        for digit in digits:
            number += roman_digits[digit]
        return number
