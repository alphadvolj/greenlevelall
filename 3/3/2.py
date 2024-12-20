# ord, char
def capitalize(word):
    first_lower = word[0]
    return chr(ord(first_lower) - 32) + word[1:]


word = "hello"
print(capitalize(word))