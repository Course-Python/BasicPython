def args_sum(*args):
	"""
	>>> args_sum(5, 10)
	15

	>>> args_sum(20, 30, 50)
	100

	>>> args_sum(2)
	2
	"""
	return sum(args)

def my_func(*args):
	return sum(args) + 5

if __name__ == "__main__":
	import doctest
	doctest.testmod()
