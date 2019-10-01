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


def check_wall_1():
    if coords1l == gr.Point(0, 200):
        v1 = -v1


def check_block():
    if coords1r == coords2l:
        v10 = v1
        v20 = v2
        v1 = ((m1 - m2)*v10 + 2*m2*v20) / (m1 + m2)
        v1 = ((m2 - m1)*v20 + 2*m1*v10) / (m1 + m2)


def main(w):
    coords = gr.Point(200, 200)
    m1 = int(input('Enter m1: '))
    m2 = int(input('Enter m2: '))
    v2 = -1
    coords1l = gr.Point(200, 200)
    coords2l = gr.Point(300, 200)
    coords1r = add(coords1, gr.Point(40,20))
    coords2r = add(coords2, gr.Point(40,20))
    block1 = gr.Rectangle(coords1l, coords1r)
    block1.setFill('cyan')
    block1.draw(w)
    
    block2 = gr.Rectangle(coords2l,coords2r)
    block2.setFill('blue')
    block2.draw(w)

    while True:
        block1.move(v1, 0)
        gr.time.sleep(0.02)
        coords1l = gr.Point(coords1l.x + v1, coords1l.y)
        coords2l = gr.Point(coords2l.x + v2, coords2l.y)
        
        
        

    


main(w)
w.getMouse()
w.close()
