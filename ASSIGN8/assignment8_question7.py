import csv

def createDict():
    f = open('Products.csv','r')
    csvReader = csv.reader(f)
    top = ''
    for line in csvReader:
        if 'product' in line:
            top = list(line)
        else:
            aDict = {}
            line = list(line)
            for i in range (0,3):
                aDict[top[i]] = line[i]
            print(aDict)

createDict()
        
