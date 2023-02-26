

def read(file):
    f = open(file,'r')
    stuAns = []
    for line in f:
        line = line.strip('\n')
        stuAns.append(line)
    f.close()
    return stuAns

def compare(stuAns):
    corAns = ['B','D','A','A','C','A','B','A','C','D']
    corCount = 0
    corQNum = []
    incorQNum = []
    incorCount = 0
    for i in range(0,len(corAns)):
        if corAns[i] != stuAns[i]:
            incorCount += 1
            incorQNum.append(i+1)
        else:
            corCount += 1
            corQNum.append(i+1)
    return [corCount,corQNum,incorCount,incorQNum]

def write(results):
    file = open('test_results.txt','a')
    if results[0] >= 7:
        file.write('Congratulations! You passed the exam\n')
    else:
        file.write('Sorry you did not pass the exam\n')
    file.write('You answered ')
    file.write(str(results[0]))
    file.write(' correctly and ')
    file.write(str(results[2]))
    file.write(' questions incorrectly\n')
    file.write('The numbers of the questions you answered correctly are: ')
    for num in results[1]:
        file.write(str(num)+ " ")
    file.write('\n')
    file.write('The numbers of the questions you answered incorrectly are: ')
    for num in results[3]:
        file.write(str(num)+ " ")
    file.close()

def main():
    file = open('test_results.txt','w')
    file.close()
    stuAns = read('student_solution.txt')
    results = compare(stuAns)
    write(results)

main()


    
    


        
    
