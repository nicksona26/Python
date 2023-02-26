def main():
    file = input("Enter file name: ")
    countDict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    file = open(file,'r')
    for line in file:
        line = line.split()
        for word in line:
            for ch in word:
                ch = ch.lower()
                if ch == 'a' or ch == 'b' or ch == 'c' or ch == 'd' or ch == 'e' or ch == 'f' or ch == 'g' or ch == 'h' or ch == 'i' or ch == 'j' or ch == 'k' or ch == 'l' or ch == 'm' or ch == 'n' or ch == 'o' or ch == 'p' or ch == 'q' or ch == 'r' or ch == 's' or ch == 't' or ch == 'u' or ch == 'v' or ch == 'w' or ch == 'x' or ch == 'y' or ch == 'z':
                    countDict[ch] += 1
    keys = list(countDict.keys())
    vals = list(countDict.values())
    print("Letter    Count    ")
    for i in range(0,26):
        print('{0:<10}{1:<10}'.format(keys[i],vals[i]))

main()        
        
        
    
                                

