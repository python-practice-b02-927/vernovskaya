import graphics as gr

SIZE_X = 1000
SIZE_Y = 800

w = gr.GraphWin("Landscape", SIZE_X, SIZE_Y)


def sky(w):
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 400))
    sky.setFill('cyan')
    sky.draw(w)


def grass(w):
    grass = gr.Rectangle(gr.Point(0, 400), gr.Point(1000, 800))
    grass.setFill('lime')
    grass.draw(w)


def sun(w):
    sun = gr.Circle(gr.Point(100, 100), 50)
    sun.setFill('pink')
    sun.draw(w)


def house(w, h, p): #p stands for starting point, h stands for height
    body = gr.Rectangle(p, gr.Point(p.x + (4/3)*h, p.y + h))
    body.setFill('chocolate')
    body.draw(w)


def cloud(w, r, p): 
    pass


def tree(w, r):
    pass


def main(w):
    sky(w)
    grass(w)
    sun(w)
    house(w, 200, gr.Point(100, 420))
    house(w, 120, gr.Point(560, 410))
    cloud(w, 30, gr.Point(150, 50))
    cloud(w, 30, gr.Point(700, 60))
    cloud(w, 20, gr.Point(500, 70))
    tree(w, 40)
    tree(w, 30)


main(w)
w.getMouse()
w.close()
