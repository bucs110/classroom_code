import turtle
class LSystem:
    def __init__(self, a, i, d):
        self.angle = a
        self.iteration = i
        self.distance = d
        self.axiom = "FX"

    def setAxiom(self, n):
        self.axiom = n

    def applyRules(self, mystr):
        newstr = ""
        for c in mystr:
            if c == 'F':
                newstr += 'F-F++F-F'
            else:
                newstr += c
        return newstr

    def createLSystem(self):
        result = self.axiom
        for i in range(self.iteration):
            result = self.applyRules(result)
        self.result = result

    def visualize(self):
        drawer = turtle.Turtle()
        drawer.speed(0)
        win = turtle.Screen()
        win.tracer(10)
        for cmd in self.result:
            if cmd == 'F':
                drawer.forward(self.distance)
            if cmd == '+':
                drawer.right(self.angle)
            if cmd == '-':
                drawer.left(self.angle)
        win.exitonclick()

def main():
        ls = LSystem(60, 10, 5)

        ls.setAxiom("FFFF")
        
        ls.createLSystem()
        ls.visualize()
        ls2 = LSystem(90, 5, 10)
        ls2.createLSystem()
        ls2.visualize()
main()
