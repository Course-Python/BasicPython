class Company:
	def __init__(self):
		self.people = []

	def add_person(self, person):
		self.people.append(person)

	def show_people(self):
		print('Company people:')
		for person in self.people:
			person.full_name()
