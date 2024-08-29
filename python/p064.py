from generators import irrational
from libraries.numeric import is_square

N = 10000
odd_period = 0
for n in range(2, N + 1):
    if is_square(n):
        continue
    term_series = irrational.root_terms(n)
    terms = [next(term_series)]
    while (t := next(term_series)) not in terms[1:]:
        terms.append(t)
    if len(terms) % 2 == 0:
        odd_period += 1
print(odd_period)
