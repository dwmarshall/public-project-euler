from math import ceil, log10

pandigital = {}

a = 10
for a in range(1, 10000):
    for b in range(a, 10000):
        if ceil(log10(a)) + ceil(log10(b)) + ceil(log10(a * b)) >= 10:
            break
        product = a * b
        candidate = "".join(sorted(str(a) + str(b) + str(product)))
        if candidate == "123456789":
            print(f"winner! {a} * {b} is {product}")
            pandigital[product] = (a, b)

print(pandigital)
print(sum(pandigital))
