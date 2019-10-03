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

def main():
    p1 = Point(0,0)
    p2 = Point(0,0)
    p3 = Point(0,0)
    p4 = Point(0,0)

    p1.num_points += 1
    p2.num_points += 5
    print(p1.num_points, p2.num_points, p3.num_points, p4.num_points)

main()
