x1 = float(input("Enter circle1's center x coordinate "))
y1 = float(input("Enter circle1's center y coordinate "))
r1 = float(input("Enter circle1's radius"))
x2 = float(input("Enter circle2's center x coordinate "))
y2 = float(input("Enter circle2's center y coordinate "))
r2 = float(input("Enter circle2's radius"))

d = ((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))**0.5

if d + r2 <= r1:
    print("circle2 is inside circle1")
elif d <= r1 +r2:
    print("circle2 overlaps circle1")
else:
    print("circle2 does not overlap circle1")
    


