binary_number= int (input("Enter Binary Number: "))
constant_number = binary_number
counter = 0
sum=0
while binary_number>0:
	singular_number = binary_number%10
	binary_changer = singular_number * (2**counter)
	sum+=binary_changer
	binary_number=binary_number//10
	counter+=1
print(f"The decimal of the binary number {constant_number} is {sum}")