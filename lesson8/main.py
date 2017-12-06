with open('input.txt', 'r') as file_input:
	print('*************')
	# print(f.read())
	for line in file_input.readlines():
		print('>> {}'.format(line))
	print('*************')


with open('output.txt', 'w') as f:
	f.write('Hello, world!\n')
	f.write('Hello, world2!')


with open():
