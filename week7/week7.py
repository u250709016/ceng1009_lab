def sumTo(n):
    total= n*(n+1)/2
    return total

print(sumTo(10))
n=int(input("enter a number: "))
print(sumTo(n))

import turtle

def drawStar(t,n,size):
    angle=180-100/n
    for i in range(n):
        t.fd(size)
        t.right(angle)

wn = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)
drawStar(t, -11, 100)
wn.exitonclick()
def sumTo(n):
    total = 0
    for i in range(1, n+1):
        total += i
        return total
print(sumTo(10))
n = int(input("enter a number"))
print(sumTo(n))

import math
