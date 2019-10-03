import turtle

class LSystem:
    def __init__(self, axiom, angle, distance, iters, rul):
        self.axiom = axiom
        self.result = ''
        self.iterations = iters
        self.distance = distance
        self.angle = angle
        self.rules = rul

    def applyRules(self, char):
        return self.rules.get(char, char)

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
        state = []
        for ch in self.result:
            if(ch == 'F'):
                t.forward(self.distance)
            elif(ch == '+'):
                t.right(self.angle)
            elif(ch == '-'):
                t.left(self.angle)
            elif(ch == ']'):
                if state:
                    t.__dict__ = state.pop()
            elif(ch == '['):
                state.append({k:v for (k,v) in t.__dict__.items()})

        wn.exitonclick()

    def __str__(self):
        return self.result

def main():
    rules = {}
    ls = LSystem("X", 90, 10, 10, rules)
    ls.createLSystem()
    print(ls)
    ls.drawLSystem()
main()
