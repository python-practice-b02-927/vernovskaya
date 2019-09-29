import graphics as gr

SIZE_X = 1000
SIZE_Y = 800

w = gr.GraphWin("Landscape", SIZE_X, SIZE_Y)


def sky():
    pass


def grass():
    pass


def main(w):
    sky(w)
    grass(w)

main(w)
w.getMouse()
w.close()
