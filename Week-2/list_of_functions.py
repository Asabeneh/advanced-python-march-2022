def add_two_numbers(a, b):
	return a + b

def make_square(n):
	return n ** 2

def calculate_circle_area(r):
	import math
	return math.pi * r ** 2

def change_string_list_to_uppercase(lst):
	new_list = []
	for item in lst:
		new_list.append(item.upper())
	return new_list
	
def revese_list(lst):
	new_lst = []
	for i in range(len(lst)-1, -1, -1):
		new_lst.append(lst[i])
	return new_lst