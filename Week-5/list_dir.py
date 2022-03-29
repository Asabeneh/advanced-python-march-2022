import os

os.chdir('../Week-4')
# os.mkdir('it_shoulb_be_in_week-4')
# os.rmdir('it_shoulb_be_in_week-4')

# print(os.getcwd())
# os.mkdir('')

print(os.listdir())
files = os.listdir()
for file in files:
	print(file)