from functools import reduce


def get_c(a, b):
    return int((a * a + b * b) ** 0.5)


def make_triplets(n):
    return [
        (a, b, c)
        for a in range(1, n)
        for b in range(a, n)
        if (c := get_c(a, b)) and a * a + b * b == c * c and a + b + c == n
    ]


def max2(a, b):
    n1, l1 = a
    n2, l2 = b
    if l1 > l2:
        return (n1, l1)
    else:
        return (n2, l2)


triplets = [(p, len(make_triplets(p))) for p in range(1001)]
largest = reduce(max2, triplets)

print(largest[0])
