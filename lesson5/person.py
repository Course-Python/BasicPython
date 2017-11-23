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

	# @staticmethod
	@classmethod
	def show_info(cls):
		return '{}: ${}'.format(cls.role, cls.salary)

	def get_description(self):
		description = super().get_description()
		description += ' ${}'.format(self.salary)
		return description


# e1 = Employee('John', 'Doe')
# e2 = Employee('John', 'Doe')
# print(e1.role)
# print(e1.salary)
# print(e2.role)
# print(e2.salary)
# print(Employee.role)
# print(Employee.salary)
# print(e.get_description())


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
	salary = 2000


# print(Employee.show_info())
# print(Manager.show_info())
# print(Administrator.show_info())
# print(Developer.show_info())


print(Owner('John', 'Doe').get_description())
print(Manager('James', 'Smith').get_description())
print(Administrator('Test', 'Admin').get_description())
print(Developer('Python', '3').get_description())

# p = Person('John', 'Doe')
# print(p.role)

