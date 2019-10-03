import turtle

def process(oldstr):
    newstr = ""
    for ch in oldstr:
        if ch == 'F':
            newstr += 'F-F++F-F'
        else:
            newstr += ch
    return newstr


def createLSystem(axiom, iters):
    end_string = ""
    for i in range(iters):
        end_string = process(axiom)
        axiom = end_string
    return end_string

def drawLSystem(instructions, angle, distance):
    snappy = turtle.Turtle()
    snappy.speed(0)
    wn = turtle.Screen()

    for cmd in instructions:
        if(cmd == 'F'):
            snappy.forward(distance)
        elif(cmd == '+'):
            snappy.right(angle)
        elif(cmd == '-'):
            snappy.left(angle)

    wn.exitonclick()

def main():
    result = createLSystem("F", 10)
    print(result)
    drawLSystem(result, 90, 10)
main()
