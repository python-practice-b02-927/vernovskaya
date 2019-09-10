#!/usr/bin/python3

from pyrob.api import *


def fill_upper_lower():
	if not wall_is_beneath():
		move_down()
		fill_cell()
		move_up()
	if not wall_is_above():
		move_up()
		fill_cell()
		move_down()


def custom_fill_cells():
	if wall_is_above() and wall_is_beneath():
		fill_cell()
	else:
		fill_upper_lower()


@task
def task_8_11():
	while True:
		custom_fill_cells()
		if wall_is_on_the_right():
			break
		move_right()


if __name__ == '__main__':
	run_tasks()
