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
