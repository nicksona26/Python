import random
import statistics

def create(f1):
    file = open(f1,'w')
    rank = ['assistant','associate','full']
    for i in range(1,1001):
        i = str(i)
        file.write('FirstName'+i+" ")
        file.write('LastName'+i+" ")
        wRank = rank[random.randint(0,2)]
        file.write(wRank)
        file.write(" ")
        if wRank == 'assistant':
            sal = random.uniform(50000,80000)
        elif wRank == 'associate':
            sal = random.uniform(60000,110000)
        elif wRank == 'full':
            sal = random.uniform(75000,130000)
        file.write('{0:.2f}'.format(sal))
        file.write('\n')
    file.close()

def stats(f1):
    file = open(f1,'r')
    totAssoc = []
    totAssist = []
    totFull = []
    totAll = []
    for line in file:
        line = line.split()
        totAll.append(float(line[3]))
        if 'assistant' in line:
            totAssist.append(float(line[3]))
        elif 'associate' in line:
            totAssoc.append(float(line[3]))
        elif 'full' in line:
            totFull.append(float(line[3]))
    file.close()
    avgAssoc = statistics.mean(totAssoc)
    avgAssist = statistics.mean(totAssist)
    avgFull = statistics.mean(totFull)
    avgAll = statistics.mean(totAll)
    print("Total salary for assistant professors:",sum(totAssist))
    print("Total salary for associate professors:",sum(totAssoc))
    print("Total salary for full professors:",sum(totFull))
    print("Total salary for all professors:",sum(totAll))
    print("Average salary for assistant professors:",avgAssist)
    print("Average salary for associate professors:",avgAssoc)
    print("Average salary for full professors:",avgFull)
    print("Average salary for all professors:",avgAll)

def main():   
    create('salary.txt')
    stats('salary.txt')

main()
            
        
        
