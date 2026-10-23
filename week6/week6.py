import turtle
# -- setup --
wn = turtle.Screen()
wn.bgcolor("green")
tess = turtle.Turtle()
# -- functions --


def drawPoly(someturtle, somesides, somesize):
    angle = 360 / somesides
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(angle)
def drawSpiral(someturtle, angle):
    size =  2
    for i in range(100):
        someturtle.forward(size)
        someturtle.right(angle)
        size = size + 1

def drawEquitriangle(someturtle, somesize):
 drawSpiral(someturtle, 3, somesize)

def drawStar(someturtle, size):
 for i in range(5):
     someturtle.forward(size)
     someturtle.right(144)

def drawSprite(someturtle, legs, length):
 angle = 360 / legs
 for i in range(legs):
     someturtle.forward(length)
     someturtle.backward(length)
     someturtle.left(angle)

# -- Exercises --
# Exercise 1
# tess.color("hotpink")
# drawPoly(tess, 8, 50)



# Exercise 2
# tess.color("blue")
# for i in range(20):
#     drawPoly(tess, 4, 100)
#     tess.left(18)


# Exercise 3
# tess.pencolor("blue")
# tess.penup()
# tess.goto(-150, 0)
# tess.pendown()
# drawSpiral(tess, 90)
#
# tess.penup()
# tess.goto(150, 0)
# tess.pendown()
# drawSpiral(tess, 89)

# # -- Exercise4 --
# drawEquitriangle(tess, 100)

# -- Exercise5 --
# tess.color("hotpink")
# tess.penup()
# tess.goto(-150, 0)
# tess.pendown()
#
# for i in range(5):
#     drawStar(tess, 100)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()
#
#
# -- Exercise6 --
drawSprite(tess, 15, 120)

# -- finish --


wn.exitonclick()