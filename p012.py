from generators import polygonal
from libraries import numeric

N = 500

t = polygonal.triangular_numbers()

while True:
    if numeric.number_of_divisors(n := next(t)) > N:
        print(n)
        break