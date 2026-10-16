# import random
# for i in range(10):
#     print(random.random())

# for i in range(10):
#     print(random.randint(25,35))

# import math
# def hypotenuse(x,y):
#     return math.hypot(x,y)
# print(hypotenuse(6,8))

# import math
#
# a = int(input("enter a: "))
# b = int(input("enter b: "))
#
# c = math.sqrt(a**2 + b**2)
# print("hypotenuse = ", c)


# import math
# def areaOfCircle(r):
#     return math.pi * r**2
# print(areaOfCircle(5))

# import turtle
# wn = turtle.Turtle()
# screen = turtle.Screen()
#
# # def drawStar():
#     for i in range(5):
#         wn.forward(100)
#         wn.right(144)
#
#         drawStar()
# screen.exitonclick()
#
# def drawStar2(t,side):
#     for i in range(5):
#         t.forward(side)
#         t.right(144)
#
# drawStar2(wn,100)
# screen.exitonclick()


# import turtle
# wn = turtle.Turtle()
# screen = turtle.Screen()
# wn.color("lightpink")
# screen.bgcolor("lightgreen")
# wn.pensize(5)

def drawSquare(t, side):
    for i in range(4):
        t.forward(side)
        t.left(90)

# for i in range(5):
#     drawSquare(wn,20)
#     wn.penup()
#     wn.forward(30)
#     wn.pendown()
#
#
# screen.exitonclick()
import turtle

wn = turtle.Turtle()
screen = turtle.Screen()
wn.color("lightpink")
screen.bgcolor("lightgreen")
wn.pensize(7)

for i in range(50, 300, 50):
    drawSquare(wn,i)
    wn.penup()
    wn.backward(25)
    wn.right(90)
    wn.forward(25)
    wn.left(90)
    wn.pendown()




screen.exitonclick()