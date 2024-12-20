def fib(n):
    a, b = 1, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


print(fib(10))