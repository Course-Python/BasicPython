a = [1, 2, 3, 4]

sum_of_elements = 0

for element in a:
	if element == 3:
		# print('This element is 3. Prev sum: {}'.format(sum_of_elements))
		continue
	sum_of_elements = sum_of_elements + element
else:
	print('Non break')

print(sum_of_elements)

# i = 0

# while True:
# 	print(i)
# 	i = i + 1
# 	if i > 5:
# 		break
