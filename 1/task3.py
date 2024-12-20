PN = ["2", "1", "+", "3", "*"]

stack = [PN]

for token in PN:
    if token in ["+", "-", "*", "/"]:
        b = stack.pop()
        a = stack.pop()

        if token == "+":
            result = a + b
        elif token == "-":
            result = a - b
        elif token == "*":
            result = a * b
        elif token == "/":
            result = a / b
        stack.append(result)

    else:
        stack.append(int(token))


print(result)