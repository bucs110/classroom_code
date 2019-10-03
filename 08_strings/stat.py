import turtle

def processString(val):
    result = ""
    for c in val:
        if(c == "F"):
            result += "F-F+FF-F"
        else:
            result += c
    return result

def createLSystem(axiom, iters):
    start = axiom
    end = ""
    for i in range(iters):
        end = processString(start)
        start = end
    return end

def visualize(result):
    distance = 15
    angle = 90
    frank = turtle.Turtle()
    frank.speed(0)
    for i in result:
        if(i == "F"):
            frank.forward(distance)
        elif(i == "-"):
            frank.left(angle)
        elif(i == "+"):
            frank.right(angle)


def main():
    result = createLSystem("F", 10)
    print(result)
    visualize(result)
main()
