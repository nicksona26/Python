def main():
    f1 = open('GirlNames.txt','r')
    girlNames = []
    for line in f1:
        line = line.strip('\n')
        girlNames.append(line)
    f1.close()
    f2 = open('BoyNames.txt','r')
    boyNames = []
    for line in f2:
        line = line.strip('\n')
        boyNames.append(line)
    f2.close()
    inp1 = input("Enter a boy's name, or N if you do no wish to enter a boy's name ")
    inp2 = input("Enter a girl's name, or N if you do not wish to enter a girl's name ")
    if inp1 == 'N':
        print("You chose not to enter a boy's name")
    else:
        if inp1 in boyNames:
            print(inp1,"is one of the most popular boy names")
        else:
            print(inp1,"is not one of the most popular boy names")            
    if inp2 == 'N':
        print("You chose not to enter a girl's name")
    else:
        if inp2 in girlNames:
            print(inp2,"is one of the most popular girl names")
        else:
            print(inp2,"is not one of the most popular girl names")
    

main()
        
