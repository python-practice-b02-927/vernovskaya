import turtle
import math


t = turtle.Turtle()
t.shape('turtle')



def angle(i,r):
    t.left(90 + 180/i)
    for k in range(i):
        t.forward(2*r*math.sin(math.pi/i))
        t.left(360/i)
    t.right(90 + 180/i)
    t.penup()
    t.forward(20)
    t.pendown()
    

r = 20    
for i in range(3, 13):
    angle(i,r)
    r = r + 20
    print(r)
	
input()
