import turtle

t = turtle.Turtle()
t.shape('turtle')


t.left(90)

def semicircle(i):
	for k in range(int(i/2)):
		t.forward(1)
		t.right(360/i)

for i in range(10):
	semicircle(200)
	semicircle(50)
	

	
	
input()
