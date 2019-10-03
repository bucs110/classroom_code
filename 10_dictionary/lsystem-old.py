import turtle

class LSystem:
    def __init__(self, axiom, angle, distance, iters):
        self.axiom = axiom
        self.result = ''
        self.iterations = iters
        self.distance = distance
        self.angle = angle

    def applyRules(self, char):
        return_str = ""
        if(char == "X"):
            return_str = "X+YF"
        elif(char == "Y"):
            return_str = "FX-Y"
        else:
            return_str = char
        return return_str

    def createLSystem(self):
        self.result = self.axiom
        for i in range(self.iterations):
            new_str = ''
            for c in self.result:
                new_str += self.applyRules(c)
            self.result = new_str

    def drawLSystem(self):
        t = turtle.Turtle()
        t.speed(0)
        wn = turtle.Screen()
        t.goto(-(wn.window_width()/2), -(wn.window_height()/2))

        print(t.__dict__)
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
