
class Animal:
    uID = 1

    def __init__(self, name, type="dog"):
        self.name = name
        self.type = type
        Animal.uID = Animal.uID + 1
        self.ID = Animal.uID
        self.arrival = time.strtime("%d/%m/%y")
        self.departure = None

    def adopted (self):
        if(self.departure == None):
            self.departure = time.strtime("%d/%m/%y")

    def bark(self):
        print("bark")

fido = Animal("Fido")
#3 days later
fido.adoption()
mittens = Animal("Mittens", "Cat")
del mittens
