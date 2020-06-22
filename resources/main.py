
def foo(plist):
    plist[0] = -1

def bar(x, y, z):
    x = 5
    return x

def main():
    mylist = [1, 2]
    mylist[0] = 3
    foo(mylist) #[-1, 2]
    bar(mylist[1]) #[-1, 2]
    print(mylist) #[-1, 2]
main()
