sum = 0
product = 1
score = int(input ("Enter Score: "))
smallest = score 
largest = score
sum += score
product *= score 
for number in range (1,4): 
	score = int(input ("Enter Score: "))
	sum += score
	product *= score 
	if score<smallest:
		smallest = score
	if score>largest:
		largest = score
	
average=sum/4
print ("Sum: ",sum)
print ("Product: ", product)
print ("Average: ", average)
print ("Smallest: ", smallest)
print ("Largest: ",largest)