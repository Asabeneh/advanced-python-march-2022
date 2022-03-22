# .txt
# .xml
# .json
# .csv
# .tsv

# data can be divided into stuctured and unstructured

# string, boolean, number(int, float, complex), list, set, tuple, dictionary
''' f = open('./sample.txt')
txt = f.read().splitlines()
print(txt)
f.close() '''

with open('./sample.txt') as f:
	lines = f.read().splitlines()
	words = []
	for line in lines:
		words.extend(line.lower().split(' '))
	print(words)

names = ['Daria','Irina','Heikki','Timo','Vesa','Imran','Ismo']
from datetime import datetime
now = datetime.now()
time_access = now.strftime("%d %B %Y, %H:%M")
print(now)
with open('names.txt', 'w') as f:
	for i, name in enumerate(names):
		f.write(f'{i + 1} - {name} is attend Advanced Python on {time_access}.\n')


	



# print(f)
# print(dir(f))