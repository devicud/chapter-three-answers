passes = 0
failures = 0
for student in range(10):
	result = int(input('Enter result (1=pass, 2=fail): '))
	while result!=1 and result!=2:
		print ("Invalid input")
		result = int(input('Enter result (1=pass, 2=fail): '))
	if result == 1:
		passes = passes + 1
	elif result == 2:
		failures = failures + 1
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
	print('Bonus to instructor')