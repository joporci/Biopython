height= raw_input("Enter height: ")
a = '*'
b = ' '
while height != '':
	for i in range(-int(height),0):
		print b*(int(height)+i)      +     a*-i
	height= raw_input("Enter height: ")
