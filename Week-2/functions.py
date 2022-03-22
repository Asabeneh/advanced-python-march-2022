# Function
import math
import random
""" from unicodedata import name
def add_two_numbers(a, b):
	return a + b


print(add_two_numbers(3, 4))
print(add_two_numbers(30, 40))
print(add_two_numbers(-3, 4))
print(add_two_numbers(1, 99))
print(add_two_numbers(-3, 3))

def make_square(n):
	return n * n

print(make_square(3))
print(make_square(10)) """

# The name of the function calculate_circle_area and it takes radius as a parameter and it return the area of the circle.

def calculate_circle_area(r):
	return math.pi * r ** 2

# write a function name change_names_to_uppercase, it takes list of strings and it returns the list strings in upper case form
names = ['Daria','Irina','Heikki','Timo','Vesa','Imran','Ismo']

countries = ['Finland', 'Sweden', 'Norway','Denmark', 'Iceland']

""" def change_string_list_to_uppercase(lst):
	new_list = []
	for item in lst:
		new_list.append(item.upper())
	return new_list

print(change_string_list_to_uppercase(names))
print(change_string_list_to_uppercase(countries)) """

nums = [3, 2, 4, 5, 1, 6]
""" 
def revese_list(lst):
	new_lst = []
	for i in range(len(lst)-1, -1, -1):
		new_lst.append(lst[i])
	return new_lst

print(revese_list(nums))
print(revese_list(names))
print(revese_list(countries)) """

# Write a function called generate_id. It takes an integer and it returns a stirng of id
# print(generate_random_id(5)) # a2bcd
# print(generate_random_id()) # 
# '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 
""" print(random.random()) # 0 > 0.99999
print(random.randint(0, 10))
print(math.floor(9.6))
print(math.floor(random.random() * 62)) """





