
def mult(x, y):
	"""
	multiplies the hard way
	args: x(int) - operand, y(int) - operand
	return: (int) result of mulitplying parameters
	"""
	accum = 0
	for i in range(y):
		accum = accum + x
	return accum

def power(x, y):
	"""
		raises a value to a power
		args: x(int) - value, y(int) - exponent
		return: (int) - result
	"""
	accum = 1
	for i in range(y):
		accum = accum * x
	return accum

def square(n):
	""
	return mult(n, n)

def main():
	print(power(5, 3))
	print(mult(5, 3))
	print(square(5))
main()
