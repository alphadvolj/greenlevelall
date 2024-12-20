import math


def distance(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1

    pifagor = math.sqrt(x * x + y * y)

    return (pifagor)


distance(10, 20, 20, 30)