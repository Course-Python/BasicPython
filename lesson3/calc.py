def read_vars():
	number1 = int(input('Enter first number: '))
	action = input('Enter action: ')
	number2 = int(input('Enter second number: '))
	return number1, action, number2

def calculate(n1, action, n2):
	function_result = None

	if action == "+":
		function_result = n1 + n2
	elif action == "-":
		function_result = n1 - n2
	elif action == "*":
		function_result = n1 * n2
	elif action == "/":
		function_result = n1 / n2

	return function_result

def print_result(result):
	print('Result: {}'.format(result))

def run_calc():
	print_result(calculate(*read_vars()))


while True:
	run_calc()
	answer = input('Continue?(y/n)')
	if answer == 'n':
		break
