import graphics as gr

window = gr.GraphWin("Jenkslex and Ganzz project", 1000, 1000)

sky = gr.Rectangle(gr.Point(0, 0), gr.Point(800, 500))
sky.setFill('magenta')

grass = gr.Rectangle(gr.Point(0, 500), gr.Point(800, 1000))
grass.setFill('green')

house = gr.Rectangle(gr.Point(500, 200), gr.Point(700, 600))
house.setFill('grey')

lake = gr.Oval(gr.Point(100, 600), gr.Point(400, 700))
lake.setFill('cyan')

sun = gr.Circle(gr.Point(300, 300), 50)
sun.setFill('orange')



sky.draw(window)
grass.draw(window)
house.draw(window)

lake.draw(window)
sun.draw(window)

for i in range(7):
    lights = gr.Rectangle(gr.Point(560, 230 + i*50), gr.Point(590, 260 + i*50))
    lights.setFill('yellow')
    lights.draw(window)

for i in range(7):
    lights1 = gr.Rectangle(gr.Point(610, 230 + i*50), gr.Point(640, 260 + i*50))
    lights1.setFill('yellow')
    lights1.draw(window)

for i in range(3):
    tree = gr.Polygon(gr.Point(100, 360 - i*10), gr.Point(80, 390 - i*10), gr.Point(150, 390 - i*10))
    tree.setFill('green')
    tree.draw(window)


window.getMouse()

window.close()
