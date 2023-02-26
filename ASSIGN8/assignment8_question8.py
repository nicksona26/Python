def sumColumn(m,colInd):
    sum = 0
    for i in range(0,3):
        sum += m[i][colInd]
    return sum

def main():
    r0 = input('Enter a 3 by 4 matrix row 0 ')
    r0 = r0.split()
    row0 = []
    for num in r0:
        num = float(num)
        row0.append(num)
    r1 = input('Enter a 3 by 4 matrix row 1 ')
    r1 = r1.split()
    row1 = []
    for num in r1:
        num = float(num)
        row1.append(num)
    r2 = input('Enter a 3 by 4 matrix row 2 ')
    r2 = r2.split()
    row2 = []
    for num in r2:
        num = float(num)
        row2.append(num)
    m = [row0,row1,row2]
    print(m)
    print('Sum of the elements at column 0 is',sumColumn(m,0))
    print('Sum of the elements at column 1 is',sumColumn(m,1))    
    print('Sum of the elements at column 2 is',sumColumn(m,2))
    print('Sum of the elements at column 3 is',sumColumn(m,3))

    
main()
