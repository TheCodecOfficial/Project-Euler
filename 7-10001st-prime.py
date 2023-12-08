from utils import is_prime

primes = []
n = 2
while len(primes) < 10001:
    while not is_prime(n):
        n += 1
    primes.append(n)
    n += 1

print(primes[-1])
