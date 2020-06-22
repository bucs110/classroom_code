#modules
import random
import turtle #gui library
#namespacing
window = turtle.Screen()
michelangelo = turtle.Turtle()
michelangelo.shape("turtle")
michelangelo.color("orange")
michelangelo.forward(50)
michelangelo.left(60)
michelangelo.forward(50)
michelangelo.setpos(0, 0)
window.exitonclick()

#Two Programming Principles
# DRY: Don't Repeat Yourself
# Write for Reuse: Write generic code that
# can be used in many situations
