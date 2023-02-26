x0 = float(input("enter x coordinate for p0 "))
y0 = float(input("enter y coordinate for p0 "))
x1 = float(input("enter x coordinate for p1 "))
y1 = float(input("enter y coordinate for p1 "))
x2 = float(input("enter x coordinate for p2 "))
y2 = float(input("enter y coordinate for p2 "))
p0= str(x0),str(y0)
p1= str(x1),str(y1)
p2= str(x2), str(y2)
if (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0) > 0:
    print("p2 is on the left side of the line")
elif (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0) == 0:
    print("p2 is on the same line")
else:
    print("p2 is on the right side of the line")

import turtle
turtle.penup()
turtle.goto(x0,y0)
turtle.write(p0,)
turtle.pendown()
turtle.goto(x1,y1)
turtle.penup()
turtle.write(p1)
turtle.goto(x2,y2)
turtle.dot()
if (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0) > 0:
    turtle.write("p2 is on the left side of the line")
elif (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0) == 0:
    turtle.write("p2 is on the same line")
else:
    turtle.write("p2 is on the right side of the line")
    
    



