#!/usr/bin/python3

from pyrob.api import *


@task (delay = 0.01)
def task_7_5():
    i = 1
    move_right()
    fill_cell()
    
    while not wall_is_on_the_right():
        for k in range(i):
            if wall_is_on_the_right():
                i = 0
                break
            move_right()
        if i == 0:
            break
        i += 1
        if not wall_is_on_the_right():
            fill_cell()
        
        


if __name__ == '__main__':
    run_tasks()
