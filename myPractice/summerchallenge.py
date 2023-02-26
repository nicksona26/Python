totalAlt = float(input("Enter starting altitude: "))
amntPeakPit = int(input("How many peaks or pits will you encounter on your journey?"))
i=0
totalDist = 0
while i < amntPeakPit:
    dist=float(input("what is the distance to the next peak or pit?"))
    alt=float(input("what is the altitude of the next peak or pit?"))
    totalDist += dist
    if alt >= totalAlt:
        temp = alt-totalAlt
        totalAlt += temp
    elif alt < totAlt:
        totalAlt -= alt
    i+=1
print(totalAlt)
print(totalDist)
