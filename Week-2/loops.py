""" for i in range(10, -1, -1):
	print(i) """

countries = ['Finland', 'Sweden', 'Norway','Denmark', 'Iceland']
# print(len(countries))
# for i in range(len(countries)):
# 	print(i + 1, countries[i])

""" for index, value in enumerate(countries):
	print(index + 1, value) """

# for country in countries:
# 	if 'land' in country:
# 		print(country)

evens = list(range(0, 101, 2))
print(evens)

odds = list(range(1, 101, 2))
print(odds)

names = ['Daria','Irina','Heikki','Timo','Vesa','Imran','Ismo']
""" for name in names:
	print(name, name.upper()) """

names_ends_with_a = []
for name in names:
	if name.endswith('a'):
		names_ends_with_a.append(name)
print(names_ends_with_a)


countries = ['Finland', 'Sweden', 'Norway','Denmark', 'Iceland']
new_countries = []
for i, v in enumerate(countries):
	new_countries.append([i + 1, v, v.upper(), v.upper()[0:3], len(v)])
print(new_countries)

count = 11

while count >= 0:
	print(count)
	count = count - 1
