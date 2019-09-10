#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while True:
        
        if not wall_is_beneath():
            move_down()
            continue
        while wall_is_beneath():
            if wall_is_on_the_left():
                while wall_is_beneath():
                    move_right()
                    if wall_is_on_the_right() and wall_is_beneath():
                        while not wall_is_on_the_left():
                            move_left()
                        return 0
                continue
            move_left()
        move_down()
        
    

if __name__ == '__main__':
    run_tasks()
