import graphics as gr

SIZE_X = 800
SIZE_Y = 400

w = gr.GraphWin("Collisions", SIZE_X, SIZE_Y)

coords = gr.Point(200, 200)

velocity = gr.Point(-1, 0)

def add(point_1, point_2):
    new_point = Point(point_1.x + point_2.x,
                      point_1.y + point_2.y)

    return new_point


def draw_block1(coords):
    block1 = gr.Rectangle(coords, coords )
    block2.setFill('cyan')
    
    block1.draw(w)


def draw_block2(coords):
    block2 = gr.Rectangle(coords, coords )
    block2.setFill('blue')
    
    block2.draw(w)


def clear_window():
    pass


def check_wall():
    pass


def check_other_block():
    pass


def main(w):
    pass


main(w)
w.getMouse()
w.close()
