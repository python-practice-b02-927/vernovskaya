import turtle

t = turtle.Turtle()
t.shape('turtle')

def star(m):
    for i in range(m):
        t.forward(200)
        t.right(180 - 180*(2*m - 1)/m)


t.left(180)
star(5)

t.penup()
t.goto(400, 0)
t.pendown()
star(11)

input()
