#6-determine a metropoly
city=raw_input("Enter city name: ")		#prompt user for city name
capital=raw_input("Is it capital: ")
popn=int(raw_input("Enter popn size: "))	#prompt user for size of population
income=raw_input("Enter amount of income: ")	#prompt user for average amount of income
if (capital == 'y' and popn > 100000) or (popn > 200000 and income >= 720000000): #determine choice
	print city,"is a metropoly."
elif popn < 100000:				#incase choice 1 above is non fulfiled choice 2 taken
	print city,"is not metropoly."
elif (capital == 'n' and popn < 200000) and (income < 720000000):
	print city, "is not a metropoly because population and income low and not a capital city ."
else:						#incase the above two choices are not satisfied
	print city,"is not a metropoly."

