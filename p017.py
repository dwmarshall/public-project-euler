N = 1000

digit_letters = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
teen_letters = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens_letters = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

def letters(n):
    if n < 10:
        return digit_letters[n]
    elif n < 20:
        return teen_letters[n - 10]
    elif n < 100:
        return tens_letters[n // 10] + digit_letters[n % 10]
    elif n < 1000:
        count = digit_letters[n // 100] + 7
        if n % 100 > 0:
            count += 3 + letters(n % 100)
        return count
    else:
        return 11 # 'one thousand'

sum = 0

for i in range(1,N+1):
    sum += letters(i)

print(sum)
