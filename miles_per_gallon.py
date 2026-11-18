gallons_counter = 0
gallons = 0
sum_of_gallons  = 0
sum_of_miles = 0
while gallons != -1:
	gallons =  int (input("Enter the gallons used (-1 to end): "))
	if gallons == -1:
		break
	miles = int (input("Enter the miles driven: "))
	miles_per_gallon = miles/gallons
	sum_of_gallons += gallons
	sum_of_miles += miles
	print ("The miles/gallon for this tank was ",miles_per_gallon)
total_miles_per_gallon = sum_of_miles/sum_of_gallons
print ("The overall average miles/gallon was ",total_miles_per_gallon)