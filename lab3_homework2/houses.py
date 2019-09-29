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


def house(w, h, p): #p stands for starting point, h stands for height
    pass


def cloud(w, r, p): 
    pass


def tree(w):
    pass


def main(w):
    sky(w)
    grass(w)
    sun(w)
    house(w, 500, gr.Point(100, 500))
    house(w, 300, gr.Point(500, 500))
    cloud(w, 30, gr.Point(150, 50))
    cloud(w, 30, gr.Point(700, 60))
    cloud(w, 20, gr.Point(500, 70))
    tree(w)
    tree(w)


main(w)
w.getMouse()
w.close()
