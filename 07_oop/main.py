
class Point:
    num_points = 0
    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor
        Point.num_points += 1


    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y**2)) ** 0.5

    def halfway(self, other):
        self.x = (self.x + other.x) / 2
        self.y = (self.y + other.y) / 2


def main():
    p1 = Point(3, 5)
    p2 = Point(2, 7)
    p3 = Point(2, 7)
    print(p1.num_points)
    print(p2.num_points)
    print(p3.num_points)
main()
