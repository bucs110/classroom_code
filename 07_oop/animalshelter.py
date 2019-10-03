class Animal:
    cid = 0
    def __init__(self, name, type="Dog"):
        self.name = name
        self.type = type
        self.date = time.strftime("%d/%m/%Y")
        Animal.cid += 1
        self.id = Animal.cid
        self.adopted = None

    def adopt(self):
        self.adopted = time.strftime("%d/%m/%Y")

def foo():
    a1 = Animal("Zelda")
    a1.adopt()
    print(a1.adopted)

def main():
    foo()
    foo()
main()
