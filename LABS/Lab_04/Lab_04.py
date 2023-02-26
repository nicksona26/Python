sen = 0
x = int(input("Enter an integer, the input ends if it is 0 "))
oddcount = 0
threeCount = 0
fiveCount = 0
oddacc = 0
threeAcc = 0
fiveAcc = 0
if x == sen:
    print("no numbers are entered except 0")
else:
    while x != sen:
             
        if x % 2 == 1 or x == 1:
            oddcount += 1
            oddacc += x   
        if x % 3 == 0:
            threeCount += 1
            threeAcc += x
        if x % 5 == 0 and x % 10 != 0:
            fiveCount += 1
            fiveAcc += x
        x = int(input("Enter an integer, the input ends if it is 0 "))

            

    print("The number of odd integers is ",oddcount)
    print("The number of integers divisible by 3 is ",threeCount)
    print("The number of integers divisible by 5 but not 10 is ",fiveCount)
    print("The sum of odd integers is ",oddacc)
    print("The sum of integers divisible by 3 is ",threeAcc)
    print("The sum of integers divisible by 5 but not 10 is ",fiveAcc)

    oddAvg = oddacc / oddcount
    threeAvg = threeAcc / threeCount
    fiveAvg = fiveAcc / fiveCount

    if (oddAvg < threeAvg) and (oddAvg < fiveAvg):
        print("The smallest average is average of odd integers ",oddAvg)
    elif (threeAvg < oddAvg) and (threeAvg < fiveAvg):
        print("The smallest average is average of integers divisible by 3 ",threeAvg)
    elif (fiveAvg < oddAvg) and (fiveAvg < threeAvg):
        print("The smallest average is average of integers divisble by 5 but not 10 ",fiveAvg)
    elif (fiveAvg == oddAvg):
        print("The smallest averages are the averages of integers divisible by 5 but not 10 ",fiveAvg," and average of odd integers ",oddAvg)
    elif (fiveAvg == threeAvg):
        print("The smallest averages are the averages of integers divisible by 5 but not 10 ",fiveAvg," and average of integers divisible by three ",threeAvg)
    elif (threeAvg == oddAvg):
        print("The smallest averages are the averages of integers divisible by 3 ",threeAvg," and average of odd integers ",oddAvg)
            
        
        
        

