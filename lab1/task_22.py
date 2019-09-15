#!/usr/bin/python3

from pyrob.api import *


@task (delay = 0.01)
def task_5_10():
    k = 0
    m = 0
    if wall_is_beneath():
        if wall_is_on_the_right():
            fill_cell()
            return
        while not wall_is_beneath():
            fill_cell()
            move_down()
        fill_cell()
        return
    while not wall_is_beneath():
        move_down()
        k = k + 1
    while not wall_is_on_the_right():
        move_right()
        m = m + 1
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()
    

    for j in range(k+1):
        if wall_is_on_the_left():
            fill_cell()
            for i in range(m):
                move_right()
                fill_cell()
        elif wall_is_on_the_right():
            fill_cell()
            for i in range(m):
                move_left()
                fill_cell()
        if j != k:
            move_down()
    if wall_is_on_the_right():
        move_left(n=m)
        


if __name__ == '__main__':
    run_tasks()
