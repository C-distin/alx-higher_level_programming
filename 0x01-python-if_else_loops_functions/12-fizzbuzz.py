#!/usr/bin/python3
def fizzbuzz():
	for i in range(1, 100):
		if i % 3 == 0 and i % 5 == 0:
			word = "FizzBuzz"
		elif i % 3 == 0:
			word = "Fizz"
		elif i % 5 == 0:
			word = "Buzz"
		else:
			word = str(i)
		print("{:s}".format(word), end=" ")