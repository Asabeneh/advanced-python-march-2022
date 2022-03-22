def generate_random_id(n = 6):
	letters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	id = ''
	max = len(letters) - 1
	for i in range(n):
		index = random.randint(0, max)
		id += letters[index]
	return id

print(generate_random_id())
print(generate_random_id(3))
print(generate_random_id(24))