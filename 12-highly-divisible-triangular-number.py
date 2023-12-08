def get_divisors(n):
    divisors = set()
    for k in range(1, int(n**0.5)):
        if n % k == 0:
            divisors.add(k)
            divisors.add(int(n / k))
    return len(divisors)


def Δ(n):
    return int((n * n + n) / 2)


n = 0
while get_divisors(Δ(n)) < 500:
    n += 1

print(Δ(n))
