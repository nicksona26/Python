import random
winner = random.randint(100,999)
ticket = int(input("Enter your lottery pick(three digits): "))

num1 = ticket % 10
temp = ticket // 10
num2 = temp % 10
temp = temp // 10
num3 = temp % 10
temp = temp // 10

x1 = winner % 10
temp2 = winner // 10
x2 = temp2 % 10
temp2 = temp2 // 10
x3 = temp2 % 10
temp2 = temp2 // 10

print("Lottery is ", winner)

if ticket == winner:
    print("Exact match: you win $10,000")
elif (num1 == x1 or num1 == x2 or num1 == x3) and (num2 == x1 or num2 == x2 or num2 == x3) and (num3 == x1 or num3 == x2 or num3 == x3):
    print("Match all digits: you win $3,000")
elif (num1 == x1 or num1 == x2 or num1 == x3) or (num2 == x1 or num2 == x2 or num2 == x3) or (num3 == x1 or num3 == x2 or num3 == x3):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
