import random



def isDivisible(x, y):
    return x % y == 0

def main():
    num = int(input("Please guess a number:"))
    y = 5
    if(isDivisible(num, y)):
        print("it's divisible!")
main()
