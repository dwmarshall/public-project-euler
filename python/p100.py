from generators import pell

# We can do the algebra and determine that if that
# if we have B blue and R red and want the chance
# of drawing two blue to be exactly one half, then
# B = (2 * R + 1 + sqrt(8 * R * R + 1)) / 2

# For B to be an integer, then 8 * R * R + 1 must be
# square, some M^2, so this becomes M * M - 8 * R * R = 1
# which is a Pell equation!

# Furthermore, M must be odd so that (2 * R + 1 + M) / 2
# is an integer

N = 1_000_000_000_000

gen = pell.equation(D=8)

while True:
    m, R = next(gen)
    if m % 2 == 0:
        continue
    B = (2 * R + 1 + m) // 2
    print(f"{R} red, {B} blue, {R + B} total")
    if R + B >= N:
        break
