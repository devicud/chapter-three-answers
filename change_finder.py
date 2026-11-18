cents = int (input("Enter amount in cents: "))
quarters = 30
quarter_counter = 0
dimes = 5
dimes_counter = 0
pennies = 1
pennies_counter = 0
if cents>quarters:
	quarter_counter= cents//quarters
	cents = cents%quarters
if cents>dimes:
	dimes_counter = cents//dimes
	cents = cents % dimes
if cents > pennies:
	pennies_counter = cents//pennies
print (f"Your change is: \n{quarter_counter} Quarters\n{dimes_counter} Dimes\n{pennies_counter} Pennies")