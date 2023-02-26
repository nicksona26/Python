import random

def main():
    k = random.randint(3,10)
    oldList = input("Enter {0} values on the same line: ".format(k))
    oldList = oldList.split()
    for i in range (0,k):
        oldList[i] = int(oldList[i])
    print("Old List:",oldList)
    print("Collapse List:",collapse(oldList))
          
def collapse(oldList):
    colList = []
    for i in range(0,len(oldList),2):
        if len(oldList) % 2 == 0:
            sm = oldList[i] + oldList[i+1]
            colList.append(sm)
        else:
            if i == len(oldList)-1:
                colList.append(oldList[i])
            else:
                sm = oldList[i] + oldList[i+1]
                colList.append(sm)     
    return colList

main()


        


    
