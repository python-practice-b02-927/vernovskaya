#!/usr/bin/python3

from pyrob.api import *

def fill_upper_lower_cell():
        if not wall_is_above():
                move_up()
                fill_cell()
                move_down()
        if not wall_is_beneath():
                move_down()
                fill_cell()
                move_up()

@task (delay = 0.01)

def task_8_10():
	while True:
		fill_upper_lower_cell()
		if wall_is_on_the_right():
			break
		move_right()


if __name__ == '__main__':
	run_tasks()
