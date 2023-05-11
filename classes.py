import pygame
from config import *
from math import *


class Myline():
    def __init__(self, surface, point1, point2, color=green) -> None:
        self.x1, self.y1 = point1
        # self.y1 = y1
        self.x2, self.y2 = point2
        # self.y2 = y2
        self.surface = surface
        self.color = color
    
    def move(self, dx, dy):
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy

    def rotate(self, alpha, point):
        self.x1, self.y1 = rotate_around_point_highperf((self.x1, self.y1), alpha, point)
        self.x2, self.y2 = rotate_around_point_highperf((self.x2, self.y2), alpha, point)

    def scale(self, factor, point=None):
        oldx1 = self.x1
        oldx2 = self.x2

        oldy1 = self.y1
        oldy2 = self.y2
        
        if point == None:
            self.x1 = oldx1 * factor
            self.x2 = oldx2 * factor
            self.y1 = oldy1 * factor
            self.y2 = oldy2 * factor
        else:
            x, y = point
            self.x1 = (oldx1 - x) * factor + x
            self.x2 = (oldx2 - x) * factor + x
            self.y1 = (oldy1 - y) * factor + y
            self.y2 = (oldy2 - y) * factor + y
    
    def recolor(self, newcolor):
        self.color = newcolor

    def update(self):
        pygame.draw.line(self.surface, self.color, (self.x1, self.y1), (self.x2, self.y2))

class Mypolygon():
    def __init__(self, surface, points, color=white) -> None:
        self.color = color
        self.surface = surface
        self.points = points
        self.lines = self.create_lines()

    def create_lines(self):
        lines = []
        for i in range(len(self.points) - 1):
            line = Myline(self.surface, self.points[i], self.points[i + 1], self.color)
            lines.append(line)
        line = Myline(self.surface, self.points[0], self.points[i + 1], self.color)
        lines.append(line)
        return lines
    
    def rotate(self, alpha, point):
        for line in self.lines:
            line.rotate(alpha, point)
    
    def move(self, dx, dy):
        for line in self.lines:
            line.move(dx, dy)

    def scale(self, factor, point=None):
        for line in self.lines:
            line.scale(factor, point)

    def update(self):
        for line in self.lines:
            line.update()

def rotate_around_point_highperf(xy, radians, origin=(0, 0)):
    """Rotate a point around a given point.
    
    I call this the "high performance" version since we're caching some
    values that are needed >1 time. It's less readable than the previous
    function but it's faster.
    """
    x, y = xy
    offset_x, offset_y = origin
    adjusted_x = (x - offset_x)
    adjusted_y = (y - offset_y)
    cos_rad = cos(radians)
    sin_rad = sin(radians)
    qx = offset_x + cos_rad * adjusted_x + sin_rad * adjusted_y
    qy = offset_y + -sin_rad * adjusted_x + cos_rad * adjusted_y

    return qx, qy