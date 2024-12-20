# ДЗ №2 
##Володащик Дмитрий К0409-23

## Задача 1
задача 1) проверить на правильность закрытых скобочек. Если все скобки закрыты верно, то алгоритм должен вывести значение True. Предлагается подумать как эту задачу можно сделать с помощью dict 

a = "(({[]}))" # True
b = "{(})" # False
c = '([])[[]]' # True
b = ")())[[]]" # False
b = "(())[[]]" # True
b = '([])' # True
```python
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
```

## Задача 2
<https://leetcode.com/problems/merge-two-sorted-lists/description/>

Вместо данных на вход предлагаю альтернативу:

first_list = deque([1,3,5,7])
second_list = deque([2,4,6,8])

В ответе должен быть deque == [1,2,3,4,5,6,7,8]
```python
first_list = [1, 3, 5, 7]
second_list = [2, 4, 6, 8]

deque = (first_list + second_list)
deque.sort()
print(deque)
```
---
### не опять, а снова

![](https://images.techinsider.ru/upload/img_cache/ff7/ff76775fd52c9ba2edabf9f26b466411_cropped_510x383.webp)
