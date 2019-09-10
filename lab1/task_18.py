#!/usr/bin/python3

from pyrob.api import *

def quit(): # я думала, выход снизу тоже может быть
    if not wall_is_above():
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()
    elif not wall_is_beneath():
        while not wall_is_beneath():
            move_down()
        while not wall_is_on_the_left():
            move_left()
        while not wall_is_above():
            move_up()

@task
def task_8_28():
    while True:
        if not wall_is_above() or not wall_is_beneath():
            quit()
            return 0
        if wall_is_on_the_left():
            while True:
                move_right()
                if not wall_is_above() or not wall_is_beneath():
                    quit()
                    return 0
        move_left()
                
    
            


if __name__ == '__main__':
    run_tasks()
