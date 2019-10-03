

def foo():
    num = input("Please enter a number:")
    try:
        num = int(num)
        better_num = 5/num
        even_better_num = math.sqrt(num)
    except ZeroDivisionError as bob:
        print(bob)
    except ValueError as bill:
        print(bill)
    except TypeError as fred:
        print(fred)

def main():
    foo()
main()
