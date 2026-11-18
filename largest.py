score = int(input ("Enter Score: "))
smallest = score 
largest = score
for number in range (1,10): 
	score = int(input ("Enter Score: "))
	if score<smallest:
		smallest = score
	if score>largest:
		largest = score
	
print ("Smallest: ", smallest)
print ("Largest: ",largest)