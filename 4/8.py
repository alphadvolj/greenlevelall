def long_strings(strings):
    for s in strings:
        if len(s) > 3:
            yield s

long_strs = long_strings(["А", "ААА", "ААААА", "ААААААА", "АААААААААААА"])
print(list(long_strs))