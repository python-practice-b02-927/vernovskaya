import turtle

t = turtle.Turtle()
t.shape('turtle')

def semicircle(i):
    for k in range(int(i/2)):
        t.forward(1)
        t.left(360/i)

def circle(i):
    for k in range(i):
        t.forward(1)
        t.right(360/i)

def eye():
    t.begin_fill()
    t.fillcolor("blue")
    circle(100)
    t.end_fill()

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

t.begin_fill()
circle(700)
t.fillcolor("yellow")
t.end_fill()

move(-50, -30)

eye()

move(50, -30)

eye()

move(0, -60)

t.width(6)
t.right(90)
t.forward(50)

move(-50, -150)

t.color("red")
semicircle(3000)
