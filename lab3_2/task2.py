import graphics as gr

SIZE_X = 1000
SIZE_Y = 800

w = gr.GraphWin("Landscape", SIZE_X, SIZE_Y)

def draw_background(w):
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 300))
    sky.setFill('cyan')
    sky.draw(w)

def draw_water(w):
    water = gr.Rectangle(gr.Point(0, 300), gr.Point(1000, 500))
    water.setFill('blue')
    water.draw(w)

def draw_sand(w):
    sand = gr.Rectangle(gr.Point(0, 500), gr.Point(1000, 800))
    sand.setFill('yellow')
    sand.draw(w)

def draw_sun(w):
    sun = gr.Circle(gr.Point(700, 80), 50)
    sun.setFill('yellow')
    sun.draw(w)

def draw_umbrella(w):
    stick = gr.Rectangle(gr.Point(100, 400), gr.Point(110, 700))
    stick.setFill('brown')
    material = gr.Polygon(gr.Point(110, 400), gr.Point(100, 400), gr.Point(5, 470), gr.Point(205, 470))
    material.setFill('pink')
    stick.draw(w)
    material.draw(w)

def draw_cloud(w):
    for i in range(3):
        circle1 = gr.Circle(gr.Point(70 + 30*i, 80), 30)
        circle1.setFill('white')
        circle1.draw(w)
    for i in range(4):
        circle1 = gr.Circle(gr.Point(70 + 30*i, 100), 30)
        circle1.setFill('white')
        circle1.draw(w)

def draw_ship(w):
    pass

def main(w):
    draw_background(w)
    draw_water(w)
    draw_sand(w)
    draw_sun(w)
    draw_umbrella(w)
    draw_cloud(w)
    draw_ship(w)

main(w)
w.getMouse()
w.close()



