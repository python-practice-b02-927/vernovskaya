import turtle

t = turtle.Turtle()
t.shape('turtle')

def circle(i):
	for k in range(i):
		t.forward(1)
		t.right(180 - 180*(i-2)/i)
	for k in range(i):
		t.forward(1)
		t.left(180 - 180*(i-2)/i)
	
t.left(90)

def semicircle(i):
	for k in range(i/2):
		t.forward(1)
		t.right(180 - 180*(i-2)/i)

for i in range(10):
	semicircle(200)
	semicircle(30)
	

	
	
input()
