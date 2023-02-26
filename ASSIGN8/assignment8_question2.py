import statistics

def main():
    f = input("Enter a filename: ")
    file = open(f,'r')
    scores = []
    for line in file:
        L = line.split()
        for score in L:
            score = int(score)
            scores.append(score)
    print(scores)
    print('There are',len(scores),'scores')
    print('The total is',sum(scores))
    print('The average is',statistics.mean(scores))
    

main()
        
