import csv

def extract(file,dataName):
    f = open(file, 'r')
    csvReader = csv.reader(f)
    for i in range(0,5):
        next(csvReader)
    disL = next(csvReader)
    colNum = disL.index(dataName)
    dataList = []
    for line in csvReader:
        num = line[colNum]
        num = num.strip('%')
        dataList.append(float(num))  
    maxx = max(dataList)
    minn = min(dataList)
    lineNum1 = dataList.index(maxx)
    lineNum2 = dataList.index(minn)
    f.seek(0)
    for i in range(0,6):
        next(csvReader)
    for i in range(0,lineNum1+1):
        if i == lineNum1:
            tLine = next(csvReader)
            maxSt = tLine[0]
        else:
            next(csvReader)
    f.seek(0)
    for i in range(0,6):
        next(csvReader)
    for i in range(0,lineNum2+1):
        if i == lineNum2:
            tLine = next(csvReader)
            minSt = tLine[0]
        else:
            next(csvReader)
    return[dataName,maxSt,maxx,minSt,minn]

def table(file,tInp):
    f = open(file,'a')
    f.write('{0:<31}:   {1:<20}{2:>15}   {3:<20}{4:>15}\n'.format(tInp[0],tInp[1],tInp[2],tInp[3],tInp[4]))
    f.close()    
        
def main():
    file = open("best_and_worst.txt", 'w')
    file.close()
    tInp1 = extract('riskfactors.csv',"Heart Disease Death Rate (2007)")
    tInp2 = extract('riskfactors.csv',"Motor Vehicle Death Rate (2009)")
    tInp3 = extract('riskfactors.csv',"Teen Birth Rate (2009)")
    tInp4 = extract('riskfactors.csv',"Adult Smoking (2010)")
    tInp5 = extract('riskfactors.csv',"Adult Obesity (2010)")
    file = open("best_and_worst.txt", 'a')
    file.write('Indicator\t\t\t\t :   Max\t\t\t                   Min\t\t\t\n')
    file.write('-----------------------------------------------------------------------------------------------------------------------------------\n')
    file.close()
    table("best_and_worst.txt",tInp1)
    table("best_and_worst.txt",tInp2)
    table("best_and_worst.txt",tInp3)
    table("best_and_worst.txt",tInp4)
    table("best_and_worst.txt",tInp5)
    
main()

