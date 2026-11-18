largest2 =0
largest =0
for number in range (1,11):
	score = int(input("Enter score: "))
	if score>largest:
		largest2 = largest
		largest = score
print (f"The largest is {largest}")
print (f"The next Largest is {largest2}")