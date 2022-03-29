# Declaring a class
class Person:
	def __init__(self, firstname, lastname, age, country, city = 'Helsinki'):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
		self.country = country
		self.city = city
		self.skills = []
	def get_person_info(self):
		number_of_skills = len(self.skills)
		statement = f'He has {number_of_skills} skills.' if number_of_skills > 0 else ''
		return f'He is {self.firstname} {self.lastname}. He is {self.age} years old and he is from {self.city}, {self.country}. {statement}'
	def add_skill(self, skill):
		self.skills.append(skill)


p1 = Person('Asabeneh', 'Yetayeh', 250, 'Finland')
p2 = Person('John','Doe', 25, 'Sweden', 'Stockholm')
print(p2.get_person_info())
p1.add_skill('Fundamentals of Python')
p1.add_skill('Advanced Python')
print(p1.skills)
print(p2.skills)
print(p1.get_person_info())


class Student(Person):
	def __init__(self, firstname, lastname, age, country, city, gender):
		super().__init__(firstname, lastname, age, country, city)
		self.points = 0
		self.hobbies = []
		self.gender = gender
	def get_person_info(self):
		pronoun = 'He' if self.gender.lower() == 'male' else 'She'
		number_of_skills = len(self.skills)
		statement = f'{pronoun} has {number_of_skills} skills.' if number_of_skills > 0 else ''
		return f'{pronoun} is {self.firstname} {self.lastname}. {pronoun} is {self.age} years old and {pronoun} is from {self.city}, {self.country}. {statement}'


s1 = Student('David', 'William', 21, 'Uk', 'London', 'Male')
s2 = Student('Marha', 'William', 19, 'Sweden', 'Stockholm', 'Female')
skills = ['HTML','CSS', 'JavaScript', 'React', 'TypeScript','Python']
for skill in skills:
	s1.add_skill(skill)
print(s1.get_person_info())
print(s2.get_person_info())
print(s1.skills)

class Stat:
	def __init__(self, lst):
		self.lst = lst

	def mean(self):
		pass
	def mode(self):
		pass
	def st_dv(self):
		pass