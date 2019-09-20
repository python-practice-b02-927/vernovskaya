#!/usr/bin/python3

from pyrob.api import *

def right_wall(m):
    fill_cell()
    move_right(n=m)
      

@task (delay = 0.01)
def task_5_10():
    k = 0
    m = 0
    
    while not wall_is_beneath():
        move_down()
        k = k + 1
    while not wall_is_on_the_right():
        move_right()
        m = m + 1
    while not wall_is_above():
        move_up()
    
    for i in range(k+1):
        for b in range(m):
            fill_cell()
            move_left()   
        if i == k:
            fill_cell()
            break
        right_wall(m)
        move_down()


if __name__ == '__main__':
    run_tasks()
