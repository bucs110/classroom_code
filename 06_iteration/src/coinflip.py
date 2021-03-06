import random
import turtle

def isInScreen(wn, t):
    left = -(wn.window_width()/2)
    right = wn.window_width()/2
    bottom = -(wn.window_height()/2)
    top = wn.window_height()/2

    x = t.xcor()
    y = t.ycor()

    if(x > right or x < left):
        return False
    if(y > top or y < bottom):
        return False
    return True

def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.shape('turtle')
    t.speed(0)
    while isInScreen(wn, t): # we can worry about this later, and just make a dummy function
        coin = random.randrange(0, 2)
        if coin == 0:           # heads
            t.left(90)
        else:                      # tails
            t.right(90)
        t.forward(20)
main()
