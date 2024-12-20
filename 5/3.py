numbers = list(range(1, 101))

sum_of_evens = sum(num for num in numbers if num % 2 == 0)

print(f"Сумма всех чётных чисел от 1 до 100: {sum_of_evens}")