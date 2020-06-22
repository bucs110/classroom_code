
def mult(x, y):
	accum = 0
	for i in range(y):
		accum = accum + x
	return accum









def power(x, y):
	accum = 1
	for i in range(y):
		accum = accum * x
	return accum









def square(n):
	return mult(n, n)


print(power(5, 3))
print(mult(5, 3))
print(square(5))
