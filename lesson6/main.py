# class MyGen:
# 	def __init__(self, number):
# 		self.number = number

# 	def __iter__(self):
# 		print('ITER!!!')
# 		return self

# 	def __next__(self):
# 		self.number -= 1
# 		if self.number < 0:
# 			raise StopIteration
# 		return self.number


# my_gen = MyGen(5)
# my_gen = MyGen(5)
# for i in my_gen:
# 	print(i)

# my_iter = [1, 2, 3, 4, 5]
# for i in my_iter:
# 	print(i)


# def my_generator(number):
# 	while number > 0:
# 		number -= 1
# 		yield number

# for i in my_generator(5):
# 	print(i)

# my_gen = my_generator(5)
# my_gen2 = my_generator(10)
# my_gen3 = my_generator(42)
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen2))
# print(next(my_gen2))
# print(next(my_gen3))
# print(next(my_gen))

# class DB:
# 	def __init__(self, name):
# 		self.name = name

# 	def open(self):
# 		print(f'Open {self.name}')

# 	def write(self, message):
# 		print(f'Write {message} to {self.name}')

# 	def close(self):
# 		print(f'Close {self.name}')

# 	def __enter__(self):
# 		self.open()
# 		return self

# 	def __exit__(self, *args):
# 		self.close()

# db = DB('database1')
# db.open()
# db.write('Hello')
# raise Exception
# db.close()

# with DB('database1') as db:
# 	db.write('Hello')
# 	raise Exception


class MyDecorator:
	def __init__(self, f):
		print('INIT decorator')
		self.f = f

	def __call__(self):
		print('CALL decorator')
		self.f()


@MyDecorator
def f():
	print('Inside f')


f()
f()
