number = int(input("Enter the number you would like to find it\'s square: "))
total = 0
square = number ** 2
for i in range(1, number +1):
    total += i * i
print(total)     