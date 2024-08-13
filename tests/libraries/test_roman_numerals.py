from libraries.roman_numeral import RomanNumeral

test_tuples = [
    ("III", 3, "III"),
    ("IV", 4, "IV"),
    ("IIII", 4, "IV"),
    ("IX", 9, "IX"),
    ("LXXXX", 90, "XC"),
    ("XC", 90, "XC"),
    ("CCLXVIIII", 269, "CCLXIX"),
]


def test_roman_to_int():
    for input, expected, _ in test_tuples:
        object = RomanNumeral(input)
        assert object.number == expected, f"Test failed for {input}"


def test_int_to_roman():
    for _, number, expected in test_tuples:
        object = RomanNumeral(number)
        assert str(object) == expected, f"Test failed for {number}"
