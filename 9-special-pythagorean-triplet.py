from utils import pythagoras

triplets = [
    (a, b, c)
    for a in range(1, 1000)
    for b in range(a, 1000)
    if (c := int(pythagoras(a, b))) and a * a + b * b == c * c and a + b + c == 1000
]
a, b, c = triplets[0]
print(a * b * c)
