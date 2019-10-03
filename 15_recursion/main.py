def fibonacciR(n):
    if(n==0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    first = 0
    second = 1
    for i in range(n):
        temp = second
        second = first + second
        first = temp
        print(first)
def main():
    fibonacciR(20)
main()
