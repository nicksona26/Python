number = int(input("enter a four digit integer: "))

x1 = number % 10
number = number // 10
x2 = number % 10
number = number // 10
x3 = number % 10
number = number // 10
x4 = number % 10
number = number // 10

print(x1, x2, x3, x4)
