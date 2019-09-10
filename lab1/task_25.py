#!/usr/bin/python3

from pyrob.api import *


@task (delay = 0.09)
def task_2_2():
    move_down(n=2)
    for i in range(5):
        fill_cell()
        move_right()
        move_up(n=2)
        for k in range(3):
            move_down()
            fill_cell()
        move_up()
        move_right()
        fill_cell()
        if i != 4:
            move_right(n=2)
    move_left(n=2)
    move_up()
        


if __name__ == '__main__':
    run_tasks()
