#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
	if wall_is_on_the_right() and wall_is_on_the_left() and wall_is_above():
		move_down()
	if wall_is_on_the_right() and wall_is_on_the_left() and wall_is_beneath():
		move_up()
	if wall_is_on_the_right() and wall_is_beneath() and wall_is_above():
		move_left()
	if wall_is_on_the_left() and wall_is_on_the_left() and wall_is_above():
		move_right()
		


if __name__ == '__main__':
	run_tasks()
