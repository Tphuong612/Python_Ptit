
from decimal import Decimal
import math


class Point:
    def __init__(self, x, y) -> None: # -> None co nghia la ko co gia tri tra ve
        self.x = x
        self.y = y
    def distance(self, p2):
        x0 = self.x - p2.x
        y0 = self.y - p2.y
        kc = math.sqrt(x0**2 + y0**2)
        return f"{kc:.4f}"

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1