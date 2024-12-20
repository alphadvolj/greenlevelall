s = input("Введите строку: ")

s = s.replace(" ", "").lower()

left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print ("Не палиндром")
        exit()
    left += 1
    right -= 1

print("Палиндром")


