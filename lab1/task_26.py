#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_2_4():
    move_down()
    for b in range(5):
        for i in range(10):
            fill_cell()
            move_right()
            move_up()
            fill_cell()
            for k in range(2):
                move_down()
                fill_cell()
            move_up()
            move_right()
            fill_cell()
            if i != 9:
                move_right(n=2)
        if b != 4:
            move_down(n=4)
        
        move_left(n=38)
    move_up()
            


if __name__ == '__main__':
    run_tasks()
