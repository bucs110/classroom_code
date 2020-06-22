import turtle

def thisIsAFunction(x): #scope
    x = x*x #local variable
x = 3
print(thisIsAFunction(abs(-1)))
