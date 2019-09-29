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


def house(w):
    pass


def cloud(w):
    pass


def main(w):
    sky(w)
    grass(w)
    sun(w)
    house(w)
    house(w)
    cloud(w)
    cloud(w)


main(w)
w.getMouse()
w.close()
