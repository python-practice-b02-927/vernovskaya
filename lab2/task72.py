import turtle
from math import sin
from math import cos
from math import pi

t = turtle.Turtle()
t.shape('turtle')

for i in range(1, 100):
	t.goto(i*sin(pi/10), i*cos(pi/10))

	
	
input()
