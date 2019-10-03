

def mult(x,y):
    accum = 0
    for i in range(y):
        accum = accum + x
    return accum

def exp(x, y):
    accum = 1
    for i in range(y):
        accum = accum * x
    return accum

def square(x):
    return mult(x, x)

#driver
def main():

main()
