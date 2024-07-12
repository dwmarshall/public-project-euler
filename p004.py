
maxPalindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if str(product) == str(product)[::-1]:
            maxPalindrome = max(maxPalindrome, product)

print(maxPalindrome)
