import turtle

t = turtle.Turtle()
t.shape('turtle')

def angle(i):
	for k in range(i):
		t.forward(20 + i*10)
		t.right(180 - 180*(i-2)/i)
	t.penup()
	t.left(90)
	t.forward(10)
	t.right(90)
	t.pendown()
	
	

for i in range(3, 13):
	angle(i)

	
	
input()
