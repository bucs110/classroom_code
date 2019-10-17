import turtle

class LSystem:
    def __init__(self, axiom, iters, angle, dist):
        self.iters = iters
        self.angle = angle
        self.dist = dist
        self.axiom = axiom
        self.result = ""

    def process(self, oldstr):
        newstr = ""
        for ch in oldstr:
            if ch == 'X':
                newstr += 'X+YF'
            elif ch == 'Y':
                newstr += 'FX-Y'
            else:
                newstr += ch
        return newstr

    def generateInstructions(self):
        self.result = self.axiom
        for i in range(self.iters):
            self.result = self.process(self.result)

    def visualize(self):
        snappy = turtle.Turtle()
        snappy.speed(0)
        wn = turtle.Screen()

        for cmd in self.result:
            if(cmd == 'F'):
                snappy.forward(self.dist)
            elif(cmd == '+'):
                snappy.right(self.angle)
            elif(cmd == '-'):
                snappy.left(self.angle)

        wn.exitonclick()

    def __str__(self):
        return self.result

########################

def main():
    #ask user input
    lsys = LSystem("FX", 10, 60, 5)
    print(lsys)
    lsys.generateInstructions()
    print(lsys)
    lsys.visualize()
main()
