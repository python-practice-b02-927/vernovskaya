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

def first_ball():
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    ballcolor = choice(colors)
    id_ = canv.create_oval(x-r,y-r,x+r,y+r,fill = ballcolor, width=0)
    d[id_] = {'x': x, 'y': y, 'r': r}
    

def move():
    global x, y, r, i, ballcolor, vx, vy
    for id_ in d:
        del d[id_]
        x = x + vx
        y = y + vy
        if x > 800 or x < 0:
            vx = -vx
        if y > 600 or y < 0:
            vy = -vy
        canv.delete(id_)
        id_ = canv.create_oval(x-r,y-r,x+r,y+r,fill = ballcolor, width=0)
        d[id_] = {'x': x, 'y': y, 'r': r, 'vx': vx, 'vy': vy}
    root.after(200, move)


def new_ball():
    global x, y, r, i, ballcolor, vx, vy
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    vx = rnd(-5,5)
    vy = rnd(-5,5)
    ballcolor = choice(colors)
    id_ = canv.create_oval(x-r,y-r,x+r,y+r,fill = ballcolor, width=0) 
    d[id_] = {'x': x, 'y': y, 'r': r, 'vx': vx, 'vy': vy}
    move()
    root.after(4000, new_ball)
    
    

def click(event):
    global count
    for id_ in d:
        if (event.x - d[id_]['x'])**2 + (event.y - d[id_]['y'])**2 <= d[id_]['r']**2:
            count += 1
            l['text'] = count
            break
    canv.delete(id_)
    new_ball()

first_ball()
new_ball()
canv.bind('<Button-1>', click)
