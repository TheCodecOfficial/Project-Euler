from utils import divisors


def divisor_sum(n):
    return sum(divisors(n, count_self=False))


def is_amicable(n):
    return (ds := divisor_sum(n)) != n and divisor_sum(ds) == n


nums = [n for n in range(10000) if is_amicable(n)]
print(sum(nums))
