
# print(), len(), max(), min(),sum, round(), input(), type, range(), list, dict, set, tuple

'''
print('Let see how print works')
print('Hello', 'World', '!')
print('How many', 'Items', 'can we put in here', 'what ever amount', 2021, True, [1, 2, 3])

'''

""" 
print(len('Hello World'))
print(len('Finland'))
print(len('Helsinki')) 

"""

""" 
print(round(9.812345))
print(round(9.812345, 2))
print(round(9.812345, 1))

"""

"""
print(min(1, 5, -5, 10, -11))
print(max(1, 5, -5, 10, -11))
print(sum([1, 5, -5, 10, -11])) 
"""


""" first_name = input('Enter your name: ')
last_name = input('Enter your lastname: ')
birth_year = input('What is your birth year? ')
full_name = firstname + ' ' + lastname
age = 2022 - int(birthyear)

print(f'You are {fullname} . You were born in {birthyear}. You are {age} years old.') """

""" a = 3
b = 4
# 3 + 4 = 7
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} x {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{b} // {a} = {b // a}')
print(f'{a} exp {b} = {a ** b}') """


""" print(range(11))
print(list(range(11)))
print(list(range(5, 21, 3))) # 5, 8,11, 14, 17, 20
print(list(range(0, 101, 2)))

even_numbers = list(range(0, 101, 2))
odd_numbers = list(range(1, 101, 2)) """

# String, Numbers(Int, Float, Complex), Booleans(True or False), List, Dictionary, Tuple, Set

first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = first_name + ' ' + last_name
age = 250
country = 'Finlnad'
city = 'Helsinki'

print(f'I am {full_name}. I live in {city}, {country}. I am {age} years old.')

print(type(10))
print(type('10'))
print(type(int('10')))
print(type(str(10)))
print(type(9.81))
print(type(1 + 2j))
print(type('Python'))
print(type([1, 2, 3, 4]))
print(type((1, 2, 3, 4)))
print(type({1, 2, 3, 4}))
print(type({'book':'kirja','house':'talo', 'student':'opiskelija'}))
print(type(list(range(3))))
