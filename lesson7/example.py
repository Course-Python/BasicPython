a1 = [1, -5, 2, -10, 3, -15, 4, -20]

# Regular
a2 = []
for e in a1:
	if not (e >= 0):
		continue
	a2.append(e)

print(a2)

# List comprehensions
print([e for e in a1 if e >= 0])

# Functinal
print(list(filter(lambda x: x >= 0, a1)))


def test():
	"""
	Test description
	"""
	pass

print(test.__doc__)


class Test:
	"""
	Class description
	"""
	pass


base_description = 'Base description. {}'


class Test2:
	__doc__ = base_description.format('Some new description from Test2')


class Test3:
	__doc__ = base_description.format('Description from Test3')


print(Test.__doc__)
print(Test2.__doc__)
print(Test3.__doc__)
