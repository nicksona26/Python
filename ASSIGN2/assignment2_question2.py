W1 = float(input("Enter weight for package 1: "))
P1 = float(input("Enter price for package 1: "))
W2 = float(input("Enter weight for package 2: "))
P2 = float(input("Enter price for package 2: "))

if (P1/W1 < P2/W2):
    print("Package 1 has the best price")
elif (P1/W1 > P2/W2):
    print("Package 2 has the best price")
else:
    print("Package 1 and Package 2 have the same price")
    
