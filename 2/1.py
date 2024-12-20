def check_parentheses(s):

    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    stack = []

    for char in s:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False

    return len(stack) == 0



print(check_parentheses("(({[]}))"))
print(check_parentheses("{(})"))
print(check_parentheses('([])[[]]'))
print(check_parentheses(")())[[]]"))
print(check_parentheses("(())[[]]"))
print(check_parentheses('([])'))