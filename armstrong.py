"""


Lets create a program to find if a number is arm strong or not


"""

def is_arm_strong(number):
	s = 0
	orginal = number
	while number > 0:
		mod = number%10
		s += pow(mod,3)
		number = number/10
	return s == orginal

upto = range(1000)

for number in upto:
	if is_arm_strong(number):
		print(number,' arm strong number')


