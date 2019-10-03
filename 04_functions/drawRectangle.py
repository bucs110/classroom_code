import turtle

def drawRect(turtle, height, width):
    turtle.down()
    for i in range(2):
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)

def main():
    h = int(input("what height rectangle?"))
    w = int(input("what width rectangle?"))
    window = turtle.Screen()
    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("green")
    print(drawRect(bob, h, w))
    window.exitonclick()

main()
