#Write a program that asks the user for a space separated list of data points (i.e. floating point numbers), then uses appropriate functions from previous questions to calculate and output the standard deviation of those numbers.
nos1 = raw_input("Enter space separated numbers: ")
def mean_mylist():
	list1=nos1.split(' ')
	total=0
	for a in list1:
		total = total + float(a)
		ave = 1.0*total/len(nos1)
		return ave
sums = 0
list2 = nos1.split(' ')
for a in list2:
	sums=sums + ((float(a) - mean_mylist())**2)
from math import sqrt
standardvariation= sqrt(sums/len(list2))
print standardvariation
