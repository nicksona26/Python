i = 2001
count = 0
while i < 2100:
    if (i % 4 == 0) and (i % 400 != 0) and (i % 100 != 0):
        print(i,end=" ")
        count += 1
        if count % 10 == 0:
            print()
    i+=1
    






    
