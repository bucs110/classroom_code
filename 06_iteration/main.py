import random
import turtle

def isInScreen(win, frank):
    leftb = -(win.window_width() / 2)
    rightb = (win.window_width() / 2)
    bottomb = -(win.window_height() / 2)
    topb = (win.window_height() / 2)

    x = frank.xcor()
    y = frank.ycor()

    if x > rightb or x < leftb:
        return False
    if y > topb or y < bottomb:
        return False
    return True

def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.shape('turtle')
    t.color('red')

    while isInScreen(wn, t):
        coin = random.choice([1, 2])
        if coin == 1:
            t.left(90)
        else:
            t.right(90)
        t.forward(50)
    wn.exitonclick()

main()
