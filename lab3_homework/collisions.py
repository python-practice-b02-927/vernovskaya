import graphics as gr
import math

SIZE_X = 800
SIZE_Y = 400

w = gr.GraphWin("Collisions", SIZE_X, SIZE_Y)

line = gr.Line(gr.Point(0, 222), gr.Point(800, 222))
line.setWidth(4)
line.setOutline('white')
line.draw(w)

count = 0


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                      point_1.y + point_2.y)
    return new_point


def check_wall_1(coords1l, v1, count):
    if coords1l.x < 0:
        v1 = -v1
        count += 1


def check_block_1(coords1r, coords2l, v1, v2, m1, m2, count):
    if coords1r.x > coords2l.x:
        v10 = v1
        v1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
        v2 = ((m2 - m1) * v2 + 2 * m1 * v10) / (m1 + m2)
        count += 1


def main(w):
    d = int(input('Enter the number of digital places: '))
    
    m1 = 1
    m2 = 100**d
    
    v1 = 0
    v2 = -5

    count = 0

    coords1l = gr.Point(200, 200)
    coords2l = gr.Point(500, 200)

    coords1r = add(coords1l, gr.Point(40, 20))
    coords2r = add(coords2l, gr.Point(40, 20))

    block1 = gr.Rectangle(coords1l, coords1r)
    block1.setFill('cyan')
    block1.draw(w)

    block2 = gr.Rectangle(coords2l,coords2r)
    block2.setFill('blue')
    block2.draw(w)

    if d == 0:
        t = 250
    elif d == 1:
        t = 300
    elif d == 2:
        t = 700
    elif d == 3:
        t = 3600
    elif d > 3:
        print('This will take up too much time. Please, try 0, 1, 2 or 3.')
        return

    for i in range(t):
        block1.move(v1, 0)
        block2.move(v2, 0)
        coords1l = gr.Point(coords1l.x + v1, coords1l.y)
        coords2l = gr.Point(coords2l.x + v2, coords2l.y)
        coords1r = gr.Point(coords1r.x + v1, coords1r.y)
        coords2r = gr.Point(coords2r.x + v2, coords2r.y)
        if coords1l.x < 0:
            v1 = -v1
            count += 1
        if coords1r.x > coords2l.x:
            v10 = v1
            v1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
            v2 = ((m2 - m1) * v2 + 2 * m1 * v10) / (m1 + m2)
            count += 1
        gr.time.sleep(0.02)

    print('pi =', count/(10**d))

    
main(w)
w.close()
