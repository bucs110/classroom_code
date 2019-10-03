
def foo(x, y):
    return (x + y) * 2

def main():
    a = 5
    b = 2
    c = 6
    d = c
    result = foo(4, 5)
    result = foo("a", "b")
    result = foo(a, c)
    result = foo(b, c)
main()
