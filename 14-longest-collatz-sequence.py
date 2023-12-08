from functools import reduce


def collatz_iteration(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def collatz_length(n):
    Σ = 1
    while n != 1:
        n = collatz_iteration(n)
        Σ += 1
    return Σ


def max2(a, b):
    n1, l1 = a
    n2, l2 = b
    if l1 > l2:
        return (n1, l1)
    else:
        return (n2, l2)


lengths = [(n, collatz_length(n)) for n in range(1, 1000000)]
longest = reduce(max2, lengths)
print(longest[0])
