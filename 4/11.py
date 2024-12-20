def square_roots(numbers):
    for num in numbers:
        if num >= 0:
            yield num ** 0.5

sqrt_gen = square_roots([4, 9, -1, 16])
print(list(sqrt_gen))