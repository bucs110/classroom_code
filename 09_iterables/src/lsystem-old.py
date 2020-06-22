import turtle

class LSystem:
    def __init__(self, axiom, angle, distance, iters):
        self.axiom = axiom
        self.result = ''
        self.iterations = iters
        self.distance = distance
        self.angle = angle

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

    def drawLSystem(self):
        t = turtle.Turtle()
        t.speed(0)
        wn = turtle.Screen()
        t.up()
        t.goto(-(wn.window_width()/2), -(wn.window_height()/2))
        t.down()

        for ch in self.result:
            if(ch == 'F'):
                t.forward(self.distance)
            elif(ch == '+'):
                t.right(self.angle)
            elif(ch == '-'):
                t.left(self.angle)

        wn.exitonclick()

    def __str__(self):
        return self.result

def main():
    ls = LSystem("FX", 90, 10, 10)
    ls.createLSystem()
    print(ls)
    ls.drawLSystem()
main()
