# от 2 до n включительно
num = int(input("Enter a number: "))
summ = 0

for i in range(2,num+1):
    summ = summ + i

print(summ)