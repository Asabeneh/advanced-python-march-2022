""" Lambda Function """

def add_two_nums(a, b):
	return a + b

print(add_two_nums(2, 3))

lambda_func = lambda x, y, z : x ** 2 + 2 * y +  z
print(lambda_func(2, 3, 1))
print(lambda_func(3, 4, 10))

nums = ['1', '4', '6']
print(nums)
print([int(n) for n in nums])

""" Higher Order Functions """


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

""" Functional Programming """

""" Functional Programming """

# map, filter, reduce

nums = [1, 2, 3, 4, 5] # [2, 4, 6, 8, 10]

""" new_nums = [n * 2 for n in nums]
evens = [n for n in nums if n % 2 != 0]
print(evens) 
"""


new_nums = list(map(lambda x: x ** 2 + 2 * x, nums))
print(new_nums)

countries = ['Finland', 'Sweden', 'Norway','Denmark', 'Iceland']
new_countries = list(map(lambda x: x.upper(), countries))
print(new_countries)

countries_with_land = list(filter(lambda x : 'land' not in x, countries))
print(countries_with_land)

evens = list(filter(lambda x : x % 2 == 0, nums))
print(evens)
# reduce is like make smoothie or mix of fruit juice
from functools import reduce

total = reduce(lambda acc, cur: acc + cur, nums)
print(total)
product = reduce(lambda a, b: a * b, nums)
print(product)

nums = [1, 2, 3, 4, 5] # [2, 4, 6, 8, 10]

total = 0
for n in nums:
	total = total + n

	"""  """

from fetch_data import fetch_data
from pprint import pprint
url = 'https://api.thecatapi.com/v1/breeds'
data = fetch_data(url)

life_spans = []
for cat in data:
	min_age = int(cat['life_span'].split(' - ')[0])
	max_age = int(cat['life_span'].split(' - ')[1])
	age = (min_age  + max_age) / 2
	life_spans.append(age)


average_life_span = (sum(life_spans) / len(life_spans))
print(round(average_life_span, 2))
print(sorted(life_spans, reverse=True))

""" Fetch Data """

def fetch_data(url):
	import requests
	response = requests.get(url)
	data = response.json()
	return data


""" Fetching Countries Data """


from fetch_data import fetch_data
from pprint import pprint
url = 'https://restcountries.com/v2/all'
data = fetch_data(url)

""" for country in data[:10]:
	languages = ', '.join(list(map(lambda l:l['name'], country['languages'])))
	print([country['name'], country['population'], country.get('capital'), languages])

print(len(data)) """


# new_lst = [[country['name'], country['population']] for country in data]
new_lst = list(map(lambda c:[c['name'], c['population']], data))
sorted_countries = sorted(new_lst, key= lambda x:x[1], reverse=True)
ten_most_populated_countries = sorted_countries[:10]
pprint(ten_most_populated_countries)