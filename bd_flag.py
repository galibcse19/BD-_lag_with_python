import turtle
obj = turtle.Turtle()
obj.speed(.9)

win = turtle.Screen()
win.bgcolor("white")

obj.penup()
obj.goto(-100, 150)
obj.pendown()
obj.begin_fill()
obj.fillcolor("seagreen")
obj.setheading(0)
obj.forward(250)
obj.setheading(270)
obj.forward(150)
obj.setheading(180)
obj.forward(250)
obj.setheading(90)
obj.forward(150)
obj.end_fill()

obj.setheading(270)
obj.forward(122)
obj.setheading(360)

obj.penup()
obj.forward(120)
obj.pendown()

obj.begin_fill()
obj.fillcolor("red")
obj.circle(50)
obj.end_fill()

obj.setheading(180)
obj.penup()
obj.forward(120)
obj.pendown()

obj.begin_fill()
obj.fillcolor("black")

obj.setheading(90)
obj.forward(150)
obj.setheading(180)
obj.forward(20)
obj.setheading(270)
obj.forward(400)
obj.setheading(180)
obj.forward(50)
obj.setheading(270)
obj.forward(30)
obj.setheading(360)
obj.forward(120)
obj.setheading(90)
obj.forward(30)
obj.setheading(180)
obj.forward(50)
obj.setheading(90)
obj.forward(400)
obj.end_fill()

obj.hideturtle()

turtle.done()