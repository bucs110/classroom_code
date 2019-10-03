import random
import os
def main():
    x = random.randrange(1,300)
    y = random.randrange(1,300)
    print(x, y)
main()

#This imports the turtle module
import turtle
#This imports the random module
import random
#This will create a light blue screen
wn = turtle.Screen()
wn.bgcolor("lightblue")
jeb = turtle.Turtle()
mitch = turtle.Turtle()
#This will make Jeb's turtle orange and Mitch's turtle blue.
jeb.color("orange")
mitch.color("blue")
#This will make both of their turtles to be shaped like actual turtles.
jeb.shape("turtle")
mitch.shape("turtle")
#This will pick up the pen so that they do not make lines.
jeb.up()
mitch.up()
#This will make them go to position (-100,20)
jeb.goto(-100,20)
mitch.goto(-100,-20)
#Race 1: This will make them go forward one at a time.
jeb.forward(random.randrange(1,300))
mitch.forward(random.randrange(1,300))
#This will reset the turtles to their original positions and prepare them for race 2.
jeb.goto(-100,20)
mitch.goto(-100,-20)
#Race 2: This will create a for loop which moves the turtles forward by 1. Then, the random function will determine how many times this loops.
randomnumbers = random.randrange(1,300)
for number in range(1, randomnumbers):
    jeb.forward(1)
    mitch.forward(1)
#This will reset the turtles to their original positions and prepare them for race 3.
jeb.goto(-100,20)
mitch.goto(-100,-20)
#Race 3: This will create a single for loop that will loop 300 times. Inside this loop, each turtle will move between 0 and 3.
for i in range(300):
  amount=random.randrange(4)
  jeb.forward(amount)
  amount=random.randrange(4)
  mitch.forward(amount)
# wn.exitonclick()

def months():
	monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
	for i in monthList:
		print("One of the months is", i)
months()
print("===END MONTH LIST===")
def numbers():
	numberList=[12,10,32,3,99]
	for i in numberList:
		print(i, i**2)
numbers()
print("===END NUMBER LIST===")

import turtle
def drawTriangle(mitch, length):
	mitch.left(30)
	mitch.forward(length)
	for i in range(2):
		mitch.left(120)
		mitch.forward(length)
		mitch.left(120)
		mitch.forward(length)

def drawSquare(mitch, length):
	for i in range(4):
		mitch.left(90)
		mitch.forward(length)

def drawHexagon(mitch, length):
	mitch.right(150)
	mitch.forward(length)
	for i in range(5):
		mitch.left(60)
		mitch.forward(50)

def drawOctagon(mitch, length):
	mitch.right(135)
	mitch.forward(50)
	for i in range(7):
		mitch.left(45)
		mitch.forward(50)

def main():
	wn = turtle.Screen()
	jeb = turtle.Turtle()
	jeb.shape("turtle")
	jeb.color("green")
	length = 50
	print(length)
	drawTriangle(jeb, length)
	drawSquare(jeb, length)
	drawHexagon(jeb,length)
	drawOctagon(jeb, length)
main()
print("===END POLYGON TURTLES===")
import turtle

sides = int(input("Please enter the number of sides in your regular polygon:"))
myvar1 = int(sides)
myvar2 = 180*myvar1
myvar3 = myvar2 - 360
myvar4 = myvar3/myvar1
print(myvar4)
sides2 = int(sides-1)
print(sides2)

length = int(input("Please enter a length"))


def drawRectangle(mitch, length):
    for i in range(sides2):
        mitch.fd(length)
        mitch.left(myvar4)

def main():
    wn = turtle.Screen()
    jeb = turtle.Turtle()
    jeb.shape("turtle")
    jeb.color(input("Please enter the desired turtle color"), input("Please enter the desired fill color"))
    jeb.begin_fill()
    drawRectangle(jeb, length)
    jeb.end_fill()
    wn.exitonclick()
main()
