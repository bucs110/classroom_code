class MyException(Exception):
    pass
class MyOtherException(Exception):
    pass

def bar():
    num = int(input("Please enter a number other than 5"))
    if num == 5:
        raise MyException()
    elif num == 3:
        raise MyOtherException()

def foo():
    bar()

def main():
    try:
        foo()
    except MyException:
        print("bar bad")
    except MyOtherException:
        print("bar bad again")


main()
