print("Kilograms   Pounds    |    Pounds   Kilograms")
strtpnd = 20
for i in range(1,200,2):
    pounds = i * 2.2
    kilograms = strtpnd * .45
    print("{0:<12}{1:<6.1f}    |    {2:<9}{3:<9.2f}".format(i,pounds,strtpnd,kilograms))
    strtpnd +=5
    
