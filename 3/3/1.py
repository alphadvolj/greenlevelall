# метод upper lower
def capitalize(word):
    first_lower = word[0]
    return first_lower.upper() + word[1:]


word = "hello"
print(capitalize(word))
