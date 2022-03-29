import os

# os.chdir('../Week-4')
# os.mkdir('it_shoulb_be_in_week-4')
# os.rmdir('it_shoulb_be_in_week-4')

# print(os.getcwd())
# os.mkdir('')


print(os.listdir())
files = os.listdir('./files')
for index, file in enumerate(files):
	cwd = os.getcwd()
	file = f'{cwd}/files/{file}'
	with open(file) as f:
		print(f'File: {index + 1} - ', f.read())
	


