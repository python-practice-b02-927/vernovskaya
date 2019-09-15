#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    k = 0
    while k != 3 and not wall_is_on_the_right():
        move_right()
        if cell_is_filled():
            k += 1
        if not cell_is_filled():
            k = 0


if __name__ == '__main__':
    run_tasks()
