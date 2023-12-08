def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]


products = [x * y for x in range(100, 1000) for y in range(100, 1000)]
palindromes = list(filter(is_palindrome, products))
print(max(palindromes))
