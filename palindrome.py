number = int(input("input number: "))
constant_number = number
reverse = 0
while number>0:
	reverse_singular = number %10
	number = number//10	
	reverse = reverse*10+ reverse_singular 

if reverse == constant_number:
	print ("This is a palindrome")
else:
	print ("This is not a palindrome")