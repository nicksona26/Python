import random
x=random.randint(1,10)
y=random.randint(1,10)
i = 1
correctCount = 0
while i <= 10:
    x=random.randint(1,10)
    y=random.randint(1,10)
    ans = int(input("what is "+str(x)+"-"+str(y)+"? "))
    if ans == (x-y):
        print("correct!")
        correctCount += 1
    else:
        print("wrong, next question")
     
    i += 1
print("you got "+str(correctCount)+" correct out of "+str(i)+" questions")

        
    
