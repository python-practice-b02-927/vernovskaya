from tkinter import *
from random import randrange as rnd, choice
import time
import sys
import json

root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']

l = Label(root, bg='black', fg='white', width=20)
l.pack()

count = 0
i = 0

d = {}
lead = {}
n = 0

name = input('Enter your name: ')


def move():
    global x, y, r, i, ballcolor, vx, vy
    canv.delete(ALL)

    for id_ in d:
        if d[id_]['x'] > 800 or d[id_]['x'] < 0:
            d[id_]['vx'] = (-1)*d[id_]['vx']
        if  d[id_]['y'] > 600 or d[id_]['y'] < 0:
            d[id_]['vy'] = (-1)*d[id_]['vy']
        d[id_]['x'] += d[id_]['vx']
        d[id_]['y'] += d[id_]['vy']
        id_ = canv.create_oval(d[id_]['x']-d[id_]['r'],d[id_]['y']-d[id_]['r'],d[id_]['x']+d[id_]['r'],d[id_]['y']+d[id_]['r'],fill = d[id_]['color'], width=0)

    root.after(200, move)


def special_ball():
    global x, y, r, i, ballcolor, vx, vy
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    vx = 12
    vy = 12
    r = 100

    id_ = canv.create_oval(x-r,y-r,x+r,y+r,fill = 'maroon', width=0) 
    d[id_] = {'x': x, 'y': y, 'r': r, 'vx': vx, 'vy': vy, 'color': 'maroon'}

    move()


def new_ball():
    global x, y, r, i, ballcolor, vx, vy
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    vx = rnd(-7,7)
    vy = rnd(-7,7)
    ballcolor = choice(colors)
    
    id_ = canv.create_oval(x-r,y-r,x+r,y+r,fill = ballcolor, width=0) 
    d[id_] = {'x': x, 'y': y, 'r': r, 'vx': vx, 'vy': vy, 'color': ballcolor}

    move()

    i += 1
    if int(i) == 15:
        root.destroy()
        lead[name] = {'name': name, 'score': count}
        with open('leaderboard.json', 'a') as f:
            json.dump(lead[name], f, indent=2)
        sys.exit(0)

    root.after(3000, new_ball)


def click(event):
    global count

    for id_ in d:
        extra = 0
        if (event.x - d[id_]['x'])**2 + (event.y - d[id_]['y'])**2 <= d[id_]['r']**2:
            if d[id_]['color'] == 'maroon':
                count += 10
            else:
                count += 1
            extra = id_
            canv.delete(id_)
            break

    if extra != 0:
       del d[extra]

    l['text'] = count
    new_ball()


new_ball()
root.after(5000, special_ball)

canv.bind('<Button-1>', click)
root.mainloop()
