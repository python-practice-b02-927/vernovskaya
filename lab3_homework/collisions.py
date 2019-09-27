import graphics as gr

SIZE_X = 800
SIZE_Y = 400

w = gr.GraphWin("Collisions", SIZE_X, SIZE_Y)

coords1 = gr.Point(200, 200)
coords2 = gr.Point(300, 200)

velocity = gr.Point(-1, 0)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                      point_1.y + point_2.y)

    return new_point


def draw_block1(coords, w):
    block1 = gr.Rectangle(coords1, add(coords1, gr.Point(40,20)))
    block1.setFill('cyan')
    
    block1.draw(w)


def draw_block2(coords, w):
    block2 = gr.Rectangle(coords2, add(coords2, gr.Point(40,20)))
    block2.setFill('blue')
    
    block2.draw(w)


def check_wall():
    pass


def check_other_block():
    pass


def main(w):
    coords = gr.Point(200, 200)
    m1 = int(input('Enter m1: '))
    m2 = int(input('Enter m2: '))
    draw_block1(coords, w)
    draw_block2(coords, w)

    


main(w)
w.getMouse()
w.close()
