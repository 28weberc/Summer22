import turtle

screen = turtle.Screen()
screen.screensize(500, 500)
screen.bgcolor("lightblue")

t = turtle.Turtle()
t.speed(0)
#sand
t.penup()
t.goto(-5000, -50)
t.pendown()
t.pencolor("bisque3")
t.fillcolor("bisque3")
t.begin_fill()
t.goto(5000, -50)
t.goto(-5000, -5000)
t.goto(5000, -5000)
t.goto(-5000, -50)
t.end_fill()
#water
t.penup()
t.goto(-5000, 0)
t.pendown()
t.fillcolor("dodgerblue4")
t.pencolor("dodgerblue4")
t.begin_fill()
t.goto(5000, 0)
t.goto(5000, -150)
t.goto(-5000, -150)
t.goto(-5000, 0)
t.end_fill()
#sun
t.penup()
t.goto(-250, 275)
t.pendown()
t.fillcolor("yellow")
t.pencolor("yellow")
t.begin_fill()
t.circle(40)
t.end_fill()
#raft
t.penup()
t.goto(100, -95)
t.pendown()
t.fillcolor("red")
t.pencolor("red")
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()
t.goto(100, -75)
t.pendown()
t.fillcolor("dodgerblue4")
t.pencolor("dodgerblue4")
t.begin_fill()
t.circle(20)
t.end_fill()


t.penup()
t.goto(75, -85)
t.pendown()
t.pencolor('white')
t.pensize(5)
t.goto(90, -75)

t.penup()
t.goto(125, -85)
t.pendown()
t.pencolor('white')
t.pensize(5)
t.goto(110, -75)

t.penup()
t.goto(75, -25)
t.pendown()
t.pencolor('white')
t.pensize(5)
t.goto(90, -35)

t.penup()
t.goto(125, -25)
t.pendown()
t.pencolor('white')
t.pensize(5)
t.goto(110, -35)





t.pensize(1)
#shark
t.penup()
t.goto(-275, -100)
t.pendown()
t.fillcolor("grey")
t.pencolor("grey")
t.begin_fill()
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)

t.circle(30,150)
t.goto(-175,-100)
t.goto(-275, -100)

t.end_fill()
#towel
t.penup()
t.setheading(0)
t.goto(-275, -350)
t.pendown()
t.fillcolor("CornflowerBlue")
t.pencolor("CornflowerBlue")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.end_fill()
#beachball
t.penup()
t.goto(-150, -300)
t.pendown()
t.fillcolor("yellow")
t.pencolor("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()
t.penup()
t.goto(-130,-300)
t.fillcolor("blue")
t.pencolor("blue")
t.begin_fill()
t.pendown()
t.circle(30)
t.end_fill()
t.penup()
t.goto(-140,-300)
t.fillcolor("red")
t.pencolor("red")
t.begin_fill()
t.pendown()
t.circle(30)
t.end_fill()
#umbrella stick
t.penup()
t.goto(250,-300)
t.fillcolor("brown")
t.pencolor("brown")
t.begin_fill()
t.pendown()
t.goto(250, -150)
t.goto(240, -150)
t.goto(240, -300)
t.goto(250, -300)
t.end_fill()
#umbrella top
t.penup()
t.goto(305, -175)
t.fillcolor("blue")
t.pencolor("blue")
t.pendown()
t.setheading(90)
t.begin_fill()
t.circle(60, 180)
t.penup()
t.goto(305, -175)
t.setheading(90)
t.pendown()
t.circle(20, 180)
t.setheading(90)
t.circle(20, 180)
t.setheading(90)
t.circle(20, 180)
t.end_fill()
#coconut
t.penup()
t.goto(150, -300)
t.fillcolor("brown")
t.pencolor("brown")
t.begin_fill()
t.pendown()
t.setheading(270)
t.circle(25, 180)
t.goto(150, -300)
t.end_fill()
t.penup()
t.goto(150, -300)
t.fillcolor("white")
t.pencolor("white")
t.begin_fill()
t.pendown()
t.goto(150, -305)
t.goto(200, -305)
t.goto(200, -300)
t.goto(150, -300)
t.end_fill()

#sunglasses
t.penup()
t.goto(50, -240)
t.fillcolor("black")
t.pencolor("black")
t.begin_fill()
t.pendown()
t.circle(10)
t.pensize(2)
t.goto(75, -240)
t.pensize(1)
t.circle(10)
t.end_fill()
t.pensize(2)
t.goto(105, -230)
t.penup()
t.goto(30, -240)
t.pendown()
t.goto(70, -220)
#text
t.penup()
t.goto(-200, 200)
t.write("Happy Summer!", font=("Arial", 15, "italic"), align="center")


























# #snowman
# t.penup()
# t.goto(200, -100)
# t.pendown()
# t.fillcolor("white")
# t.pencolor("white")
# t.begin_fill()
# t.circle(30)
# t.end_fill()
# t.penup()
# t.goto(200, -100)
# t.pendown()
# t.begin_fill()
# t.circle(20)
# t.end_fill()
# t.penup()
# t.goto(200, -100)
# t.pendown()
# t.begin_fill()
# t.circle(10)
# t.end_fill()

# #sled
# t.penup()
# t.goto(-200, -150)
# t.pendown()
# t.pencolor("brown")
# t.pensize(10)
# t.forward(100)
# t.circle(20, 180)

































turtle.done()