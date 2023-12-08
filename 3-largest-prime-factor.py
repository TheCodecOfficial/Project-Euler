from utils import is_prime

n = 600851475143
k = int(n**0.5) + 1

while not (n % k == 0 and is_prime(k)):
    k -= 1

print(k)
