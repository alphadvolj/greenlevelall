# ДЗ №3 володащик Дмитрий К0409-23

## Задача 1
Даны четыре действительных числа: $x_1, y_1, x_2, y_2$. Напишите функцию `distance(x1, y1, x2, y2)`, вычисляющая расстояние между точкой $(x_1,y_1)$ и $(x_2,y_2)$.
```python
import math

def distance (x1, y1, x2, y2):
    x = x2-x1
    y = y2-y1
    
    pifagor = math.sqrt(x*x + y*y)
    
    return (pifagor)

distance (10, 20, 20, 30)
```
## Задача 2. 
Дано действительное положительное число $a$ и целоe число $n$.
Вычислите $a^n$. Решение оформите в виде функции `power(a, n)`.
Стандартной функцией возведения в степень пользоваться нельзя.

```python
def power(a, n):
    b = a
    for i in range(n - 1):
        b = b * a

    return b


power(3, 2)
```

## Задача 3
Напишите функцию `capitalize()`, которая принимает слово из маленьких латинских букв и возвращает его же, меняя первую букву на большую.
Например, `print(capitalize('word'))` должно печатать слово `Word`.

На вход подаётся строка, состоящая из слов, разделённых одним пробелом. Слова состоят из маленьких латинских букв. Напечатайте исходную строку, сделав так, чтобы каждое слово начиналось с большой буквы. При этом используйте вашу функцию `capitalize()`.

### метод upper lower
```python
def capitalize(word):
    first_lower = word[0]
    return first_lower.upper() + word[1:]


word = "hello"
print(capitalize(word))
```
### ord, char
```python
def capitalize(word):
    first_lower = word[0]
    return chr(ord(first_lower) - 32) + word[1:]


word = "hello"
print(capitalize(word))
```
## Задача 4.
Написать рекурсивную функцию для вычисление факториала n!

```python
def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x = x * i

    return x

print(factorial(5))
```

## Задача 5
Дано действительное положительное число $a$ и целое неотрицательное число $n$. Вычислите $an$ не используя циклы, возведение в степень через `**` и функцию `math.pow()`, а используя рекуррентное соотношение $a^n=a⋅a^{n-1}$.

Решение оформите в виде функции `power(a, n)`.

```python
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

result = power(2, 3)
print(result)
```
## Задача 6
Дана последовательность целых чисел, заканчивающаяся числом 0. Выведите эту последовательность в обратном порядке.
При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных. Рекурсия вам поможет.

```python
def print_reverse():
    number = int(input("Введите число (0 для завершения): "))
    if number == 0:
        return
    print_reverse()
    print(number)

print_reverse()
```
---
### еще один кот

![](https://cdn.nur.kz/images/1120x630/0de6d3c675807aeb.jpeg)
