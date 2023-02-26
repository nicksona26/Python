def read(f):
    file = open(f,'r')
    wordList = []
    for l in file:
        line = l.split()
        for word in line:
            wordList.append(word)
    return wordList
    file.close()
        
def write(s,L):
    file = open("fileAnalysis.txt", 'a')
    file.write(s)
    if L != []:
        for word in L:
            file.write(word + " ")
        file.write("\n")
        file.close()
    
def uniqueList(L):
    uList = []
    for i in L:
        if i not in uList:
            uList.append(i)
    return uList

def unionList(UL1,UL2):
    unionList = []
    for word in UL1:
            unionList.append(word)
    for word in UL2:
        if word not in UL1:
            unionList.append(word)  
    return unionList

def commList(UL1,UL2):
    commList = []
    for word in UL1:
        if word in UL2:
            commList.append(word)    
    return commList

def wordList(UL1,UL2):
    L1 = []
    L2 = []
    for word in UL1:
        if word not in UL2:
            L1.append(word)
    for word in UL2:
        if word not in UL1:
            L2.append(word)
    return L1,L2

def wordCount(fxList,ULX):
    cList = []
    for i in fxList:
        cList.append(fxList.count(i))
    write("Word            Count\n",[])
    for i in range(0, len(ULX)):
        table = "{0:<16}{1:<5}\n".format(fxList[i],cList[i])
        write(table,[])
    write("\n",[])
        
def main():
    f1 = input("Enter the name of the first input file: ")
    f2 = input("Enter the name of the second input file: ")
    s1 = "Unique words in file 1: "
    s2 = "Unique words in file 2: "
    s3 = "Union of the words in files 1 & 2: "
    s4 = "Intersection of the words in files 1 and 2: "
    s5 = "Words in file 1 but not in file 2: "
    s6 = "Words in file 2 but not in file 1: "
    s7 = "Words in file 1 but not in file 2 and Words in file 2 but not in file 1: "
    s8 = "Frequency table for file 1: \n"
    s9 = "Frequency table for file 2: \n"
    f1List = read(f1)
    f2List = read(f2)
    UL1 = uniqueList(f1List)
    UL2 = uniqueList(f2List)
    write(s1,UL1)
    write(s2,UL2)
    write(s3,unionList(UL1,UL2))
    write(s4,commList(UL1,UL2))
    L1,L2 = wordList(UL1,UL2)
    write(s5,L1)
    write(s6,L2)
    write(s7,L1+L2)
    write(s8,[])
    wordCount(f1List,UL1)
    write(s9,[])
    wordCount(f2List,UL2)
    
main()
    
    
