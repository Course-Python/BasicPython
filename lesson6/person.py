class SalaryException(Exception):
	pass

class Person:
	role = 'Person'

	def __init__(self, first_name, second_name):
		self.first_name = first_name
		self.second_name = second_name

	@property
	def full_name(self):
		return '{} {}'.format(self.first_name, self.second_name)

	def get_description(self):
		return '{} - {}'.format(self.role, self.full_name)


class Employee(Person):
	role = 'Employee'
	salary = 1000

	@classmethod
	def show_info(cls):
		return '{}: ${}'.format(cls.role, cls.salary)

	def get_description(self):
		description = super().get_description()
		description += ' ${}'.format(self.salary)
		return description


class Owner(Person):
	role = 'Owner'


class Manager(Employee):
	role = 'Manager'
	salary = 1500


class Administrator(Employee):
	role = 'Administrator'
	salary = 1200


class Developer(Employee):
	role = 'Developer'
	__salary = 2000

	@property
	def salary(self):
		return self.__salary

	@salary.setter
	def salary(self, amount):
		if amount > 10000:
			self.__salary = 10000
		elif amount < 0:
			raise SalaryException('Salary should be > 0')
		else:
			self.__salary = amount



# print(Owner('John', 'Doe').get_description())
# print(Manager('James', 'Smith').get_description())
# print(Administrator('Test', 'Admin').get_description())

dev = Developer('Python', '3')

try:
	dev.salary = -50000000
	print('TRY AFTER dev.salary!!!')
except SalaryException as e:
	print('EXCEPT!!!')
	dev.salary = 100
except NameError as e:
	print('NameError')
finally:
	print('FINALLY!!!')

print(dev.get_description())


