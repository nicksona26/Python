#lab6
print("Feet    Meters    |    Meters    Feet")
print("--------------------------------------------")
startMeter = 20
def footToMeter(foot):
    meters = foot * .305
    return meters
def meterToFoot(meter):
    foot = meter/.305
    return foot
for i in range(1,11):
    meters = footToMeter(i)
    feet = meterToFoot(startMeter)
    print("{0:<8}{1:<6.3f}    |    {2:<10}{3:.2f}".format(i,meters,startMeter,feet))
    startMeter+=5
 
