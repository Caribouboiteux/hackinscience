#!/usr/bin/env python3

from pngcanvas import PNGCanvas
import math

HEIGHT = 10
WIDTH = int(HEIGHT * (16 / 9))

canvas = PNGCanvas(WIDTH, HEIGHT,
                   bgcolor=(255, 255, 255, 255),
                   color=(0, 0, 0, 255))


def get_point(x, y):
    """
    Return (Red, Green, Blue, Alpha) for the given (x, y) point.
    """
    R = (math.sin(x / 50) ** 2) * 0xFF
    G = (math.cos(y / 50) ** 2) * 0xFF
    B = (math.sin((x - y) / 50) ** 2) * 0xFF
    A = 0xFF
    return (int(R), int(G), int(B), int(A))

for x in range(WIDTH):
    for y in range(HEIGHT):
        canvas.point(x, y, get_point(x, y))
with open('solution.png', 'wb') as solution:
    solution.write(canvas.dump())
