#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
	while wall_is_beneath() or wall_is_above():
		if (wall_is_beneath() and not wall_is_above()) or (wall_is_above() and not wall_is_beneath()):
			fill_cell()
		if wall_is_on_the_right():
			break
		move_right()


if __name__ == '__main__':
	run_tasks()
