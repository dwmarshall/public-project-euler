from math import gcd


def is_curious_fraction(n, d):
    if n % 10 == 0 or n == d:
        return False
    n_tens, n_ones = divmod(n, 10)
    d_tens, d_ones = divmod(d, 10)
    if n_tens == d_tens and d_ones != 0:
        return n / d == n_ones / d_ones
    elif n_tens == d_ones and d_tens != 0:
        return n / d == n_ones / d_tens
    elif n_ones == d_tens and d_ones != 0:
        return n / d == n_tens / d_ones
    elif n_ones == d_ones and d_tens != 0:
        return n / d == n_tens / d_tens
    else:
        return False


net_numerator = net_denominator = 1

for n in range(10, 100):
    for d in range(n, 100):
        if is_curious_fraction(n, d):
            print(f"{n}/{d} is a curious fraction")
            net_numerator *= n
            net_denominator *= d

print(net_denominator // gcd(net_numerator, net_denominator))
