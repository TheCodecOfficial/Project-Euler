def is_double_base_palindrome(n):
    binary = bin(n)[2:]
    return str(n) == str(n)[::-1] and binary == binary[::-1]


print(sum([n for n in range(1000000) if is_double_base_palindrome(n)]))
