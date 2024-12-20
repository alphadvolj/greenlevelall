def unique_letters(s):
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
            yield char


unique_gen = unique_letters("hello")
print(list(unique_gen))