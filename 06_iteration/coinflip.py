import random
import turtle

def isInScreen(wn, t):
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
