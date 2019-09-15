#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while not cell_is_filled():
        move_up()
    move_left()
    if cell_is_filled():
        return 
    if not cell_is_filled():
        move_right(n=2)


if __name__ == '__main__':
    run_tasks()
