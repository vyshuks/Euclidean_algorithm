#python version 2.7.13
#calculates GCD of two numbers
#-----------------------------
def main():
	print "Calculate GCD";
	a = eval(raw_input("Enter first number: "));
	b = eval(raw_input("Enter second number: "));

	c = gcd(a,b)
	print "GCD of {0} and {1} = {2}" . format(a, b, c)

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)

if __name__ == '__main__':
			main()		

