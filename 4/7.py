def even_number_generator(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = even_number_generator(numbers)

for even in even_numbers:
    print(even)