import turtle

t = turtle.Turtle()
t.shape('turtle')
for i in range(1, 11):
	t.pendown()
	for k in range(4):
		t.forward(100*i)
		t.right(90)
	t.penup()
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(50)
	t.right(180)
	
	
input()
