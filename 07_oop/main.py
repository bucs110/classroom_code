import time

class Animal:
    current_id = 1
    def __init__(self, n, t="Dog"):
        self.name = n
        self.type = t
        #self.id = id(self)
        self.id = self.current_id
        Animal.current_id += 1
        self.arrived = time.strftime("%d/%m/%Y")
        self.adopted = None

    def adopt(self):
        if(self.adopted == None):
            self.adopted = time.strftime("%d/%m/%Y")

def main():
    zelda = Animal("Zelda")
    sonic = Animal("sonic", "Hedgehog")

main()
