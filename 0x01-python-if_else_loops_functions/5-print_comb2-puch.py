#!/usr/bin/python3
# a program that prints numbers from 00 to 99 separated by , , followed by a space
for i in range(10):
	for j in range(11):
		if i < j:
			print("{}{}".format(i, j), end=", ")