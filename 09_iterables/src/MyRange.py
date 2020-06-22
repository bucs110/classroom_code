class MyRange:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step

    def __iter__(self):
        self.next = self.start
        return self

    def __next__(self):
        if self.next < self.stop:
            result = self.next
            self.next = self.next+self.step
            return result
        else:
            raise StopIteration


def main():
    pt = MyRange('A')
    for n in pt:
        print(n)
    for n in pt:
        print(n)
main()
