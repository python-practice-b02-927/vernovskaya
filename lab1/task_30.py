#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    n = 1
    while not wall_is_beneath():
        n += 1
        move_down()
    while not wall_is_above():
        move_up()
    
    while n > 0:
        move_down()
        for i in range(n-2):
            fill_cell()
            move_down()
        move_right()
        for i in range(n-2):
            fill_cell()
            move_right()
        move_up()
        for i in range(n-2):
            fill_cell()
            move_up()
        move_left()
        for i in range(n-2):
            fill_cell()
            move_left()
        move_down()
        move_right()
        n = n - 2
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()
        
        


if __name__ == '__main__':
    run_tasks()
