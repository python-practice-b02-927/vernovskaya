from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']

l = Label(root, bg='black', fg='white', width=20)
l.pack()

count = 0

d = {}
n = 0

def move():
    global x, y, ballcolor
    x = x + 5
    y = y + 5
    canv.delete(ALL)
    id_ = canv.create_oval(x-r,y-r,x+r,y+r,fill = ballcolor, width=0)
    d[id_] = {'x': x, 'y': y, 'r': r}
    for id_ in d:
        id_ = canv.create_oval(x-r,y-r,x+r,y+r,fill = ballcolor, width=0)
        d[id_] = {'x': x, 'y': y, 'r': r}
    root.after(200, move)


def new_ball():
    global x, y, r, i, ballcolor
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    ballcolor = choice(colors)
    
    root.after(2000, move)
    root.after(2000, new_ball)
    

def click(event):
    global count
    for id_ in d:
        if (event.x - d[id_]['x'])**2 + (event.y - d[id_]['y'])**2 <= d[id_]['r']**2:
            count += 1
            l['text'] = count
            elem = d.pop(id_) # вынести удаление за цикл
            canv.delete(id_)
            new_ball()


new_ball()
canv.bind('<Button-1>', click)
