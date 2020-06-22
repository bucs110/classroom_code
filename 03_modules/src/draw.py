import turtle

def main():
    # print(list(range(2, 12, limit)))
    # for i in range(1, 10, 2):
    #     print(i)
    # for i in range(500, 1001):
    #     print(i)
    # for i in range(0, -11, -1):
    #     print(i)
    # for i in range(101):
    #     print(i)


    leonardo = turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor("green")
    leonardo.shape("turtle")
    for c in ["purple", "red", "orange", "green"]:
        leonardo.color(c)
        leonardo.down()
        for i in range(4):
            leonardo.forward(50)
            leonardo.left(90)
        leonardo.up()
        leonardo.forward(60)
        leonardo.shape("turtle")


    window.exitonclick()
main()
