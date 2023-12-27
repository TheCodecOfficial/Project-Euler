from utils import binomial_coeff


def num_rectangles(a, b):
    return binomial_coeff(a + 1, 2) * binomial_coeff(b + 1, 2)


pairs = (
    (a, b)
    for n in range(1, 10000000000)
    for a in range(1, n)
    for b in range(a, n)
    if a + b == n
)

nearest = 1, 1
nearest_Δ = 2000000
while pair := next(pairs):
    a, b = pair
    Δ = abs(num_rectangles(a, b) - 2000000)
    if Δ < nearest_Δ:
        nearest = a, b
        nearest_Δ = Δ
    if a > 2001 or b > 2001:
        break

print(nearest[0] * nearest[1])
