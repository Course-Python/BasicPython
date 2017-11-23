# class A:
# 	def say(self, word):
# 		print('***{}***'.format(word))

# a = A()
# a.say('Hello')  # A.say(a, 'Hello')
# a.say('world')
# a.say('123')


# a1 = A()
# a2 = A()
# print(a1.__class__)
# print(a2.__class__)


# class dict:
# 	......
# 	def get(self, key):
# 		.......
# 		return self[key]
# 	........

# l = dict()  # l = {}
# l['key'] = 'value'
# l.get('key')  # dict.get(l, 'key')

from person import Person, a
from company import Company


p1 = Person('John', 'Doe')
p2 = Person('James', 'Smith')
p3 = Person('James3', 'Smith3')

company = Company()
company.add_person(p1)
company.add_person(p2)
company.add_person(p3)
company.add_person(Person('Test', 'Test'))
company.show_people()

# p1 = Person('John', 'Doe')
# p1.full_name()

# Person('James1', 'Smith1')
# Person('James2', 'Smith2')
# Person('James3', 'Smith3')

# p1.full_name()
# p1.full_name()

# p2 = Person('James', 'Smith')

# p2.full_name()
# p2.full_name()

# p1.full_name()
