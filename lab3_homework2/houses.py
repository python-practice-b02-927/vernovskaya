import graphics as gr

SIZE_X = 1000
SIZE_Y = 800

w = gr.GraphWin("Landscape", SIZE_X, SIZE_Y)


def sky(w):
    pass


def grass(w):
    pass


def sun(w):
    pass


def house(w, h, p):
    pass


def cloud(w):
    pass


def tree(w):
    pass


def main(w):
    sky(w)
    grass(w)
    sun(w)
    house(w, 500, gr.Point(100, 500))
    house(w, 300, gr.Point(500, 500))
    cloud(w)
    cloud(w)
    cloud(w)
    tree(w)
    tree(w)


main(w)
w.getMouse()
w.close()
