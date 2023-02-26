import turtle

x = int(input("enter x coordinate for the center of the rectangle: "))
y = int(input("enter y coordinate for the center of the rectangle: "))
w = int(input("enter the width of the rectangle: "))
h = int(input("enter the height of the rectangle: "))

turtle.penup()
turtle.goto(x,y)
turtle.forward(w/2)
turtle.right(90)
turtle.pendown()
turtle.forward(h/2)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(h)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(h/2)

turtle.done()



