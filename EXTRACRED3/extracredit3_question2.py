import statistics

def getData(highs,lows):
    highs = highs.split()
    highs1 = []
    for num in highs:
        num = float(num)
        highs1.append(num)
    lows = lows.split()
    lows1 = []
    for num in lows:
        num = float(num)
        lows1.append(num)
    twoDim = []
    twoDim.append(highs1)
    twoDim.append(lows1)
    return twoDim
    
def averageHigh(twoDim):
    avg = statistics.mean(twoDim[0])
    avg = round(avg,1)
    return avg
    
def averageLow(twoDim):
    avg = statistics.mean(twoDim[1])
    avg = round(avg,1)
    return avg

def highTemp(twoDim):
    maxx = max(twoDim[0])
    return maxx

def lowTemp(twoDim):
    minn = min(twoDim[1])
    return minn

def main():
    highs = input("Enter highest temperatures for 12 months: ")
    lows = input("Enter lowest temperatures for 12 months: ")      
    twoDim = getData(highs,lows)
    print("List of the highest and lowest temperatures for each month of the year:")
    for num in twoDim[0]:
        print(num, end =" ")
    print( )
    for num in twoDim[1]:
        print(num, end = " ")
    print('\n')
    print("Average high temperature for the year:",averageHigh(twoDim))
    print("Average low temperature for the year:",averageLow(twoDim))
    print("Highest high temperature for the year:",highTemp(twoDim))
    print("Lowest low temperature for the year:",lowTemp(twoDim))

main()



