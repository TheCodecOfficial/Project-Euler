from utils import is_prime

primes = [p for p in range(2, 2000000) if is_prime(p)]
print(sum(primes))
