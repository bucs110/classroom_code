import turtle

class LSystem:
    def __init__(self, axiom, angle, distance, iters, rules):
        self.axiom = axiom
        self.result = ''
        self.iterations = iters
        self.distance = distance
        self.angle = angle
        self.rules = rules

    def process(self, oldstr):
        newstr = ""
        for ch in oldstr:
            newstr += self.rules.get(ch, ch)
        return newstr

    def generateInstructions(self):
        self.result = self.axiom
        for i in range(self.iterations):
            self.result = self.process(self.result)

    def drawLSystem(self):
        t = turtle.Turtle()
        t.speed(0)
        wn = turtle.Screen()
        t.up()
        t.goto(-(wn.window_width()/2), -(wn.window_height()/2))
        t.down()
        state = []
        for ch in self.result:
            if(ch == 'F'):
                t.forward(self.distance)
            elif(ch == '+'):
                t.right(self.angle)
            elif(ch == '-'):
                t.left(self.angle)
            elif(ch == '['):
                state.append({k:v for k,v in t.__dict__.items()})
            elif(ch == ']'):
                if(state):
                    prev_state = state.pop()
                    t.__dict__ = prev_state
        wn.exitonclick()

    def __str__(self):
        return self.result

def main():
    rules = {"X":"F[-X]+X", "F":"FF"}
    ls = LSystem("FX", 90, 10, 10, rules)
    ls.generateInstructions()
    print(ls)
    ls.drawLSystem()
main()
