class Person:
	person_count = 0

	def __init__(self, first_name, second_name):
		self.first_name = first_name
		self.second_name = second_name
		self.full_name_counter = 0
		Person.person_count += 1
		print('Person count: {}'.format(Person.person_count))

	def full_name(self):
		self.full_name_counter += 1
		print('{}. {} {}'.format(self.full_name_counter, self.first_name, self.second_name))


a = 100