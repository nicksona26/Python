#input
firstNum = int(input("Enter first number "))
secondNum = int(input("Enter second number "))
print()

#switch
if secondNum < firstNum:
    temp = secondNum
    secondNum = firstNum
    firstNum = temp

#reassignment
x = firstNum
y = secondNum
n1 = firstNum
n2 = secondNum
x1 = firstNum
x2 = secondNum

#loop1
print("Odd integers between",firstNum,"and",secondNum,"are:",end=" ")
while firstNum < secondNum:
    if firstNum % 2 != 0:
        print(firstNum,end=" ")
        firstNum += 2
    else:
        firstNum += 1
print()
print()

#loop2
acc = 0
print("Sum of even integers between",x,"and",y,"=",end=" ")
while x < y:
    if x % 2 == 0:
        x+=2
        acc += x
    else:
        x+=1
        acc += x
print(acc)
print()

#loop3
acc2 = 0
print("Integers and their square between",n1,"and",n2,"are:")
while n1 <= n2:
    sqr = n1 ** 2
    if n1 % 2 == 1:
        acc2 += sqr
    print(n1, sqr)
    n1+=1
print()
print("Sum of the squares of odd integers between",x1,"and",x2,"=",acc2)





    






        




        



    
    

        
    
