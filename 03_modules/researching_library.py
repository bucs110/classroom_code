import turtle              # 1.  import the modules

wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('green')

donatello = turtle.Turtle()    # 3.  Create two turtles
donatello.color('purple')
donatello.shape('turtle')

donatello.setheading(0)
donatello.forward(50)
donatello.setheading(90)
donatello.forward(50)
donatello.setheading(180)
donatello.forward(50)
donatello.setheading(270)
donatello.forward(50)

donatello.color('red')
donatello.up()
donatello.goto(100, 100)
donatello.down()

donatello.setheading(0)
donatello.forward(50)
donatello.setheading(90)
donatello.forward(50)
donatello.setheading(180)
donatello.forward(50)
donatello.setheading(270)
donatello.forward(50)

wn.exitonclick()
