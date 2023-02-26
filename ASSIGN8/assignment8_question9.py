def isMarkovMatrix(m):
    valid1 = False
    valid2 = False
    for L in m:
        for num in L:
            if num > 0:
                valid1 = True
    for i in range(0,3):
        sum = 0
        for j in range(0,3):
            sum += m[j][i]
    if sum == 1:
        valid2 = True
    if valid1 == True and valid2 == True:
        return "It is a Markov matrix"
    else:
        return "It is not a Markov matrix"

def main():
    m = []
    for i in range(0,3):
        inp = input("Enter a 3 by 3 matrix row by row ")
        inp = inp.split()
        mVal = []
        for num in inp:
            num = float(num)
            mVal.append(num)
        m.append(mVal)
    print(isMarkovMatrix(m))
        

main()
        
