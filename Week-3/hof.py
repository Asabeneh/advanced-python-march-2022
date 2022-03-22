# Function that take other function as a parameter
# Function that return other function

from operator import mul


def make_square(n):
	return n ** 2

def make_cube(func, n):
	return func(n) * n

print(make_square(5))
print(make_cube(make_square, 5))

def do_math(n):
	def add_ten(a = 10):
		return n + a
	return add_ten

print(do_math(5)(25))

def do_arithemtic():
	def add(a, b):
		return a + b
	def sub(a, b):
		return a - b
	def multiply(a, b):
		return a * b
	return {
		'add':add,
		'sub':sub,
		'multiply':multiply
	}
	
print(do_arithemtic()['add'](99, 1))
print(do_arithemtic()['multiply'](99, 1))