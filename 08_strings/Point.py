import turtle

class Point:
    num_points = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.num_points += 1

    def distanceFromOrigin(self):
        return (self.x**2 + self.y**2) ** 0.5

    def halfway(self, other):
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point(mx, my)

    def __str__(self):
        return "("+str(self.x) + ", "+  str(self.y) + ")"

def main():
    p1 = Point(1,4)
    p2 = Point(2,5)
    p3 = Point(3,6)
    print(p1, p2, p3)

main()
