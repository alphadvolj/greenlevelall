def print_reverse():
    number = int(input("Введите число (0 для завершения): "))
    if number == 0:
        return
    print_reverse()
    print(number)

print_reverse()