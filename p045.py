from generators import polygonal

T = polygonal.triangular_numbers()
P = polygonal.pentagonal_numbers()
H = polygonal.hexagonal_numbers()

_, t = next(T), next(T)
_, p = next(P), next(P)
_, h = next(H), next(H)

TBD = 2

while TBD:
    biggest = max(t, p, h)
    while t < biggest:
        t = next(T)
    while p < biggest:
        p = next(P)
    while h < biggest:
        h = next(H)
    if t == p and p == h:
        print(f"match on {t}")
        TBD -= 1
        t = next(T)
