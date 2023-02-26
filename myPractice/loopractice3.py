i = 0
oddlist = []
fivelist = []
evenlist = []
list = [10, 3, 5, 56, 78, 64, 33, 2, 54, 65, 5, 34]
while i <= len(list):
        if list[i] % 2 == 1:
                oddlist.append(list[i])
        if list[i] % 5 == 0:
                fivelist.append(list[i])
        if list[i] % 2 == 0:
                evenlist.append(list[i])
        i += 1
print(oddlist)
print(fivelist)
print(evenlist)


            
                
