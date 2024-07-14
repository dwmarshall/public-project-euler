N = 1000

digit_letters = [
    len(""),
    len("one"),
    len("two"),
    len("three"),
    len("four"),
    len("five"),
    len("six"),
    len("seven"),
    len("eight"),
    len("nine"),
]
teen_letters = [
    len("ten"),
    len("eleven"),
    len("twelve"),
    len("thirteen"),
    len("fourteen"),
    len("fifteen"),
    len("sixteen"),
    len("seventeen"),
    len("eighteen"),
    len("nineteen"),
]
tens_letters = [
    len(""), # zero tens
    len(""), # ten already in teen_letters
    len("twenty"),
    len("thirty"),
    len("forty"),
    len("fifty"),
    len("sixty"),
    len("seventy"),
    len("eighty"),
    len("ninety"),
]

def letters(n):
    if n < 10:
        return digit_letters[n]
    elif n < 20:
        return teen_letters[n - 10]
    elif n < 100:
        return tens_letters[n // 10] + digit_letters[n % 10]
    elif n < 1000:
        count = digit_letters[n // 100] + len("hundred")
        if n % 100 > 0:
            count += len("and") + letters(n % 100)
        return count
    else:
        return len("onethousand")

sum = 0

for i in range(1,N+1):
    sum += letters(i)

print(sum)
