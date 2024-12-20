def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

result = power(2, 3)
print(result)