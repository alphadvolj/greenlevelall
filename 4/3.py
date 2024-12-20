def count_strings_without_ab(length):
    if length == 1:
        return 2  # a b
    elif length == 2:
        return 3  #aa bb ba

    f = [0] * (length + 1)
    f[1] = 2
    f[2] = 3

    for n in range(3, length + 1):
        f[n] = f[n - 1] + f[n - 2]

    return f[length]

result = count_strings_without_ab(6)
print(result)