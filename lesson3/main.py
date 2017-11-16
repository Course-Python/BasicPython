# def print_smt(arg1, *args):
# 	print(arg1)
# 	for arg in args:
# 		print(arg)

# print_smt('hello')
# print('########################')
# print_smt('hello', 'world', '!')
# print('########################')
# my_args = ('hello', 'world', '!', 123, 'test')
# print_smt(*my_args)


# def hello(name='world'):
# 	print('Hello {}'.format(name))

# hello()
# hello('Anton')

# def print_args(arg1, arg2, arg3):
# 	print(arg1, arg2, arg3)

# print_args(10, arg3=30, arg2=20)


# def print_args(arg1, *args, **kwargs):
# 	print(arg1, kwargs.get('arg2'), kwargs.get('arg3'))

# my_kwargs = {'arg2': 'test', 'arg3': 'test2'}
# print_args(10, 15, 20, **my_kwargs)

# def get_sum(n1, n2):
# 	return n1 + n2

# get_sum_lambda = lambda n1, n2: n1 + n2

# print(get_sum_lambda(5, 10))


# 1 1 2 3 5 8 13 21

def fib(number, n1=1, n2=1):
	if number == 1:
		return n1
	else:
		return fib(number - 1, n2, n1 + n2)

print(fib(1))
print(fib(3))
print(fib(5))
print(fib(10))
print(fib(500))

