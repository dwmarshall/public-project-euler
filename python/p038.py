def pandigitalProduct(n: int) -> tuple[bool, str]:
    result = ""
    i = 1
    while len(result) < 9:
        result += str(n * i)
        i += 1
    if len(result) > 9:
        return (False, "")
    if "".join(sorted(result)) == "123456789":
        return (True, result)
    else:
        return (False, "")


maxPandigital = ""

for n in range(192, 10000):
    qualified, product = pandigitalProduct(n)
    if qualified:
        maxPandigital = max(maxPandigital, product)

print(maxPandigital)
