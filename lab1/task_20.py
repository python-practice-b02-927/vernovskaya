#!/usr/bin/python3

from pyrob.api import *



@task(delay=0.01)
def task_4_3():

    for i in range(6):
        for i in range(27):
            move_right()
            fill_cell()
        move_down()
        move_right()
        for i in range(27):
            move_left()
            fill_cell()
        move_down()
        move_left()
    move_right()
                
                    


if __name__ == '__main__':
    run_tasks()
