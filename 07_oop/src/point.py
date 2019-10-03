import turtle

class Point:
    num_points = 0

    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor
        Point.num_points += 1
        print("Num Points:", self.num_points)
        print("Num Points:", Point.num_points)

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def halfway(self, other):
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point(mx, my)

    def __str__(self):
        return "X: " + str(self.x) +", Y: " + str(self.y)

def main():
    a = Point(2, 3)
    print(a.num_points)
    a.num_points += 1
    b = Point(1, 3)
    Point.num_points += 5
    print(a.num_points)
    print(b.num_points)


main()
