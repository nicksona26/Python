def main():
    f = input("Enter a filename: ")
    rStr = input("Enter a string to be removed: ")
    file = open(f,'r')
    lines = []
    for line in file:
        L = line.replace(rStr,"")
        lines.append(L)
    file.close()
    file = open(f,'w')
    file.close()
    file = open(f,'w')
    for line in lines:
        file.write(line)
    file.close()

main()
        
    
            
        
        
            
