import random

def twoNums(op,lvl):
    if lvl == 1:
        n1 = random.randint(0,9)
        n2 = random.randint(0,9)
    elif lvl == 2:
        n1 = random.randint(10,99)
        n2 = random.randint(10,99)
    if op == "-" and n1 < n2:
        temp = n1
        n1 = n2
        n2 = temp
    if op == "/" and n2 == 0:
        n2 = 1
    if op == "/":
        print("How much is {0} {1} {2}? Round your answer to two decimals ".format(n1,op,n2))
    else:
        print("How much is {0} {1} {2}? ".format(n1,op,n2))
    return [n1,n2]

def main():
    lvl = int(input("Enter difficulty level (1 or 2): "))
    ans = 0
    corCnt = 0
    incorCnt = 0
    while ans != -1:      
        choice = menu()
        nums = twoNums(choice,lvl)
        ans = float(input("Enter your answer (-1 to exit): "))
        corResDict = {1:"Very good!",2:"Excellent",3:"Nice work!",4:"Keep up the good work!"}
        incorResDict = {1:"No. Please try again",2:"Wrong. Try once more.",3:"Don't give up!",4:"No. Keep trying"}
        res = random.randint(1,4)
        
        if choice == "+":
            corAns = nums[0] + nums[1]
        elif choice == "-":
            corAns = nums[0] - nums[1]    
        elif choice == "*":
            corAns = nums[0] * nums[1]
        else:
            corAns = nums[0] / nums[1]
            corAns = float("{0:.2f}".format(corAns))
        
        if ans == -1:
            print("Number of correct answers: ",corCnt)
            print("Number of wrong answers: ",incorCnt)
            print("Thanks for playing!")
        elif ans == corAns:
            print(corResDict[res],"\n")
            corCnt += 1
        else:
            print(incorResDict[res],"\n")
            incorCnt += 1

def menu():
    print("1 = addition\n2 = subtraction\n3 = multiplication\n4 = division\n5 = random operation")
    choice = int(input("Enter the operation (1 to 5): "))
    print()
    if choice == 5:
          choice = random.randint(1,4)
    opDict = {1:"+",2:"-",3:"*",4:"/"}
    return opDict[choice]


main()



    
    
