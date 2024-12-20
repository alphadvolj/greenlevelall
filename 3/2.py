def power(a, n):
    b = a
    for i in range(n - 1):
        b = b * a

    return b


power(3, 2)