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


def main(w):
    sky(w)
    grass(w)
    sun(w)


main(w)
w.getMouse()
w.close()
