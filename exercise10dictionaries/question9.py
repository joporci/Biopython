#Write a program the reads strings until a blank line is encountered. For each string entered, treat the portion of the string up to the first colon (or the entire string if no colon is present) as a key name, and everything after the first colon as a value. If the key portion has been entered before, print out the old value paired with that key, and then change the value to the newly entered one. After the blank line, print out a neat list of key value pairs.
string = str(raw_input("Enter a string: "))
d = {}
while string != '':
	if ':' in string:
		x=string.index(':')
		key = string[0:x]
		value = string[x+1:]
	else:
		key = string
		value = ''
	if key in d.keys():
		print key, d[key]
		d[key]=value
	else:
		d[key]=value

	string = str(raw_input("Enter a string: "))
names = list(d.items())
print names
