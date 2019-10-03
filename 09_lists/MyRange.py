class MyRange:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, start):
        self.start = start.lower()

    def __iter__(self):
        self.next = self.start
        return self

    def __next__(self):
        if self.next < 'z':
            result = self.next
            self.next = chr(ord(self.next)+1)
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
