""" def change_string_list_to_uppercase(lst):
	new_list = []
	for item in lst:
		new_list.append(item.upper())
	return new_list

print(change_string_list_to_uppercase(names))
print(change_string_list_to_uppercase(countries)) """

nums = [1, 2, 3, 4] # [2, 4, 6, 8]

""" new_nums = []
for num in nums:
	new_nums.append(num * 2)
print(new_nums) """

new_nums = [num * 2 for num in nums]

names = ['Daria','Irina','Heikki','Timo','Vesa','Imran','Ismo']
new_names_list = [name.upper() for name in names]
print(new_names_list)
names_endswith_a = [name for name in names if name.endswith('a')]
print(names_endswith_a)
