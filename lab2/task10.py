import turtle

t = turtle.Turtle()
t.shape('turtle')

def circle(i):
	for k in range(200):
		t.forward(1)
		t.right(180 - 180*(200-2)/200)
	for k in range(200):
		t.forward(1)
		t.left(180 - 180*(200-2)/200)
	

for i in range(20):
	circle(i)
	t.right(60)

	
	
input()
