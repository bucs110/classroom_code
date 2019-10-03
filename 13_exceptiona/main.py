
class MyException(Exception):
    pass
class MyOtherException(Exception):
    pass
def bar(num):
    if(num < 0):
        raise MyException()
    elif(num > 10):
        raise MyOtherException()
def foo():
    bar(-1)

def main():
    try:
        foo()
    except MyException:
        print("too low")
    except MyOtherException:
        print("too high")
main()
