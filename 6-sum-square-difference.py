sum_of_squares = sum([n * n for n in range(101)])
square_of_sum = sum([n for n in range(101)]) ** 2
print(square_of_sum - sum_of_squares)
