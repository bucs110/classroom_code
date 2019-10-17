import random

def threenp1(n):
    while n != 1:
        if n  %  2 != 0:
            n = 3 * n + 1
        else:
            n = n // 2
        print(n)

def main():
    threenp1(int(input("num? ")))

main()
