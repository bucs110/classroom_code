import turtle

class LSystem:
    def __init__(self, axiom, angle, distance, iters, rules):
        self.axiom = axiom
        self.result = ''
        self.iterations = iters
        self.distance = distance
        self.angle = angle
        self.rules = rules

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
        t.up()
        t.goto(-(wn.window_width()/2), -(wn.window_height()/2))
        t.down()
        saved_states = []
        for ch in self.result:
            if(ch == 'F'):
                t.forward(self.distance)
            elif(ch == '+'):
                t.right(self.angle)
            elif(ch == '-'):
                t.left(self.angle)
            elif(ch == '['):
                tstate = {key:value for key, value in t.__dict__.items()}
                saved_states.append(tstate)
            elif(ch == ']'):
                if(saved_states):
                    t.__dict__ = saved_states.pop()

        wn.exitonclick()

    def __str__(self):
        return self.result

def main():
    ls = LSystem("X", 25, 5, 6, {'X':'F-[[X]+X]+F[+FX]-X', 'F':'FF'})
    ls.createLSystem()
    print(ls)
    ls.drawLSystem()
main()
