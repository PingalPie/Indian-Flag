import turtle
from turtle import *
# importing module to make flag 

screen = turtle.Screen()
# screen for output

t = turtle.Turtle()
speed(0)
# Defining a turtle Instance

t.penup()
t.goto(-50, 250)
t.pendown()
# initially penup()

# Orange Rectangle
t.color("orange")
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(63)
t.right(90)
t.forward(200)
t.end_fill()
t.left(90)
t.forward(63)

# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(63)
t.left(90)
t.forward(200)
t.left(90)
t.forward(63)
t.end_fill()

# Big Blue Circle
t.penup()
t.goto(75, 155)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(31)
t.end_fill()

# Big White Circle
t.penup()
t.goto(71, 155)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(27)
t.end_fill()

# Mini Blue Circles 0
t.penup()
t.goto(72, 143)
t.pendown()
t.color("navy")
for i in range(2):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(20)
    t.pendown()

# Mini Blue Circle 1
t.penup()
t.goto(63, 179)
t.pendown()
t.color("navy")
for i in range(1):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
t.backward(10)
t.left(15)
t.pendown()

# Mini Blue Circles 2
t.penup()
t.goto(48, 184)
t.pendown()
t.color("navy")
for i in range(1):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
t.backward(10)
t.left(15)
t.pendown()

# Mini Blue Circles 3
t.penup()
t.goto(33, 179)
t.pendown()
t.color("navy")
for i in range(1):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
t.backward(10)
t.left(15)
t.pendown()

# Mini Blue Circles 4

t.penup()
t.goto(18, 164)
t.pendown()
t.color("navy")
for i in range(1):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
t.backward(10)
t.left(15)
t.pendown()

# blue circle 5
t.penup()
t.goto(21, 144)
t.pendown()
t.color("navy")
for i in range(1):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
t.backward(10)
t.right(15)
t.pendown()

# Mini Blue Circles 6
t.penup()
t.goto(34, 132)
t.pendown()
t.color("navy")
for i in range(1):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
t.backward(10)
t.left(15)
t.pendown()

# Mini Blue Circles 7
t.penup()
t.goto(49, 130)
t.pendown()
t.color("navy")
for i in range(1):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
t.backward(10)
t.left(15)
t.pendown()

# Mini Blue Circles 8
t.penup()
t.goto(60, 134)
t.pendown()
t.color("navy")
for i in range(1):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
t.backward(10)
t.left(15)
t.pendown()


# Small Blue Circle
t.penup()
t.goto(43, 160)
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

# Spokes
t.penup()
t.goto(43, 157)
t.pendown()
t.pensize(2)
for i in range(19):
    t.forward(30)
    t.backward(30)
    t.left(20)

# Pole
t.penup()
t.goto(-50, 250)
t.pendown()

t.color("black")
t.begin_fill()
t.right(-70)
t.forward(400)
t.end_fill()

# Stairs 1
t.color("orange")
t.begin_fill()
t.forward(31)
t.left(90)
t.forward(50)
t.left(90)
t.forward(31)
t.left(90)
t.forward(100)
t.left(90)
t.forward(31)
t.left(90)
t.forward(50)
t.end_fill()

# Stairs 2
t.color("navy")
t.begin_fill()
t.right(90)
t.forward(31)
t.left(90)
t.forward(100)
t.left(90)
t.forward(31)
t.left(90)
t.forward(200)
t.left(90)
t.forward(31)
t.left(90)
t.forward(100)
t.end_fill()

# Stairs 3
t.color("green")
t.begin_fill()
t.right(90)
t.forward(31)
t.left(90)
t.forward(200)
t.left(90)
t.forward(31)
t.left(90)
t.forward(400)
t.left(90)
t.forward(31)
t.left(90)
t.forward(200)
t.end_fill()

''' to hold the
output window '''
turtle.done()
