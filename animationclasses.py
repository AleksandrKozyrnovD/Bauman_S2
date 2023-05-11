from classes import *
import random

class Planet():
    def __init__(self, surface, radius, center_of_planet, center, spin, color, tolerance=1, detalization=36):
        self.radius = radius
        self.surface = surface
        self.color = color
        self.tolerance = tolerance
        self.center_of_planet = center_of_planet
        self.center = center
        self.spin = spin
        self.detalization = detalization
        self.points = self.create_circle(self.tolerance)
        self.lines = self.create_lines()
    
    def create_circle(self, tolerance):
        points = []
        for theta in range(0, 360, tolerance):
            points.append(rotate_around_point_highperf(((self.center_of_planet[0] + self.radius), self.center_of_planet[1]), radians(theta), self.center_of_planet))
        return points

    def create_lines(self):
        lines = []
        for i in range(len(self.points) - 1):
            line = Myline(self.surface, self.points[i], self.points[i + 1], self.color)
            lines.append(line)

        for i in range(self.detalization):
            line = Myline(self.surface, random.choice(self.points), random.choice(self.points), self.color)
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

    def recolor(self, newcolor):
        self.color = newcolor
        for line in self.lines:
            line.recolor(newcolor)
    
    def update(self):
        for line in self.lines:
            line.update()