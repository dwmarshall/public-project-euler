from generators import irrational
from libraries.numeric import is_square

D = 1000

maximum_d = 0
maximum_x = 0

for d in range(2, D + 1):
    if is_square(d):
        continue
    # note that we're using root_terms(d) instead of partial_quotients(sqrt(d))
    # This is because after about twenty terms, the floating point resolution
    # is exceeded.
    p_q = (t[0] for t in irrational.root_terms(d))
    for f in irrational.convergents(p_q):
        x = f.numerator
        y = f.denominator
        if x * x - d * y * y == 1:
            print(f"for {d}, x = {x}, y = {y}")
            if x > maximum_x:
                maximum_d = d
                maximum_x = x
            break
print(maximum_d)
