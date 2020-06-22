import turtle              # 1.  import the modules

wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('green')

donatello = turtle.Turtle()    # 3.  Create two turtles
donatello.color('purple')
donatello.shape('turtle')

for i in range(4):
    donatello.left(90)
    donatello.forward(50)


donatello.color('red')
donatello.up()
donatello.goto(100, 100)
donatello.down()

for i in [0,90,180,270]:
    donatello.setheading(i)
    donatello.forward(50)

wn.exitonclick()
