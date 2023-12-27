import random
import math
from functools import reduce


def product(*args):
    if not args:
        raise ValueError("At least one argument is required")

    flattened_args = [
        arg if isinstance(arg, (int, float)) else product(*arg) for arg in args
    ]
    result = reduce(lambda x, y: x * y, flattened_args)
    return result


def digit_sum(n):
    return sum(digits(n))


def digits(n):
    return [int(n) for n in str(n)]


def num_digits(n):
    return len(str(n))


def is_prime(n):
    return miller_rabin(n)
    # return is_prime_primitive(n)


def is_prime_primitive(n):
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False

    return True


def is_witness(a, n, d, s):
    x = pow(a, d, n)  # Compute a^d mod n

    if x == 1 or x == n - 1:
        return False  # a is not a witness

    for _ in range(s - 1):
        x = pow(x, 2, n)  # Compute x^2 mod n
        if x == n - 1:
            return False  # a is not a witness

    return True  # a is a witness


def miller_rabin(n, k=10):
    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n == 1:
        return False

    # Write n-1 as 2^s * d
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Perform Miller-Rabin test with k random bases
    for _ in range(k):
        a = random.randint(2, n - 2)
        if is_witness(a, n, d, s):
            return False  # n is composite

    return True  # n is likely prime


def divisors(n, count_self=True):
    divisors = set()
    for k in range(1, int(n**0.5)):
        if n % k == 0:
            divisors.add(k)
            divisors.add(int(n / k))
    if not count_self:
        divisors.discard(n)
    return list(divisors)


def binomial_coeff(n, k):
    Π = 1
    for j in range(1, k + 1):
        Π *= (n + 1 - j) / j
    return int(Π)


def pythagoras(a, b):
    return math.sqrt(a * a + b * b)
