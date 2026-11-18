number = int (input("Enter Number: "))
contant_number = number
factorial = 1

while contant_number > 0:
	factorial *= contant_number
	contant_number -= 1

print('the factorial of ',number ,'is ', factorial)