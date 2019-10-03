
def squares(num):
    accum = []
    for i in range(1, num+1):
        if(i % 2 == 0):
            accum.append(i ** 2)
    print(accum)
    #list comprehension
    accum = [i**2 for i in range(1, num+1) if(i % 2 == 0)]
    print(accum)

def main():
    num = int(input("Please enter a number: "))
    print(squares(num))
main()
