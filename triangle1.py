rows = int (input("Enter amount of rows: "))
for levels in range(1,rows+1):
	for star in range (1,levels+1):
		print("*", end = '')
	print(' ', end = '')
	for space in range(levels,rows+1,1):
		print(" ", end = '')
	for star2 in range(levels,rows+1,1):
		print("*", end = '')
	for space2 in range (1,levels+1):
		print(" ", end = '')
	for space3 in range (2,levels+1):
		print(" ", end = '')
	print(' ', end = '')
	for star3 in range(levels,rows+1,1):
		print("*", end = '')
	for space4 in range(levels,rows+1,1):
		print(" ", end = '')
	print(' ', end = '')
	for star4 in range (1,levels+1):
		print("*", end = '')
	print()