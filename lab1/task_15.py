#!/usr/bin/python3

from pyrob.api import *

def move_lower_left():
	while not wall_is_on_the_left():
		move_left()
	while not wall_is_beneath():
		move_down()


def move_lower_right():
	while not wall_is_beneath():
		move_down()
	while not wall_is_on_the_right():
		move_right()

def move_upper_left():
	while not wall_is_on_the_left():
		move_left()
	while not wall_is_above():
		move_up()

def move_upper_right():
	while not wall_is_on_the_right():
		move_right()
	while not wall_is_above():
		move_up()

@task
def task_8_21():
	if wall_is_above() and wall_is_on_the_right():
		move_lower_left()
	elif wall_is_above() and wall_is_on_the_left():
		move_lower_right()
		return
	elif wall_is_beneath() and wall_is_on_the_right():
		move_upper_left()
	elif wall_is_beneath() and wall_is_on_the_left():
		move_upper_right()


if __name__ == '__main__':
	run_tasks()
