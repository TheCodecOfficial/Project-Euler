fib = [1, 2]
while fib[-1] < 4e6:
    fib.append(fib[-1] + fib[-2])
Σ = sum(list(filter(lambda x: x % 2 == 0, fib)))
print(Σ)
