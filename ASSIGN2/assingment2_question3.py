num = int(input("enter an integer: "))

if (num % 5 == 0 and num % 6 == 0):
    print(num, " is divisible by both 5 and 6")
elif (num % 5 == 0 or num % 6 == 0):
    print(num, " is divisible by 5 or 6, but not both")
else:
    print(num, " is not divisible by either 5 or 6")
    
    
    
