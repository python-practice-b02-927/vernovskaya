import turtle

t = turtle.Turtle()
t.shape('turtle')
n = int(input())

for i in range(n):
	t.forward(100)
	t.stamp()
	t.right(180)
	t.forward(100)
	
	t.right(180 - 360/n)
	
	
input()
