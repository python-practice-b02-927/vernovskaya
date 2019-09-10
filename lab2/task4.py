import turtle

t = turtle.Turtle()
t.shape('turtle')
for i in range(200):
	t.forward(1)
	t.right(180 - 180*(200-2)/200)
	
input()
