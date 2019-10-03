
class PowTwo:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if(self.i <= self.limit):
            result = 2**self.i
            self.i += 1
            return result
        else:
            raise StopIteration

def main():
    for i in PowTwo(100):
        print(i)

main()
