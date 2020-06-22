import turtle

class LSystem:
    def __init__(self, axiom, iters, angle, dist, rules):
        self.iters = iters
        self.angle = angle
        self.dist = dist
        self.axiom = axiom
        self.result = ""
        self.rules = rules

    def process(self, oldstr):
        newstr = ""
        for ch in oldstr:
            newstr += self.rules.get(ch, ch)
        return newstr

    def generateInstructions(self):
        self.result = self.axiom
        for i in range(self.iters):
            self.result = self.process(self.result)

    def visualize(self):
        snappy = turtle.Turtle()
        snappy.speed(0)
        wn = turtle.Screen()
        state = []
        for cmd in self.result:
            if(cmd == 'F'):
                snappy.forward(self.dist)
            elif(cmd == '+'):
                snappy.right(self.angle)
            elif(cmd == '-'):
                snappy.left(self.angle)
            elif(cmd == '['):
                copy = {k:v for k,v in snappy.__dict__.items()}
                state.append(copy)
            elif(cmd == ']'):
                if state:
                    prev_state = state.pop()
                    snappy.__dict__ = prev_state


        wn.exitonclick()

    def __str__(self):
        return self.result

########################

def main():
    #ask user input
    rules = {'X':'F[-X]+X', 'F':'FF'}
    lsys = LSystem("FX", 10, 60, 5, rules)
    print(lsys)
    lsys.generateInstructions()
    print(lsys)
    lsys.visualize()
main()
