from graphics import *
from random import randint
from math import sin, cos, radians
import time

def rotateLine(line, degrees):
    angle = radians(degrees) 
    cosang, sinang = cos(angle), sin(angle)

    points = line.getPoints()
    n = len(points)
    cx = sum(p.getX() for p in points) / n
    cy = sum(p.getY() for p in points) / n

    new_points = []
    for p in points:
        x, y = p.getX(), p.getY()
        tx, ty = x-cx, y-cy
        new_x = ( tx*cosang + ty*sinang) + cx
        new_y = (-tx*sinang + ty*cosang) + cy
        new_points.append(Point(new_x, new_y))

    rotated_line = line.clone() 
    rotated_line.points = new_points
    return rotated_line


win = GraphWin('Rotate Line', 600, 600)

print("Point 1")
x1=int(input("Enter x:"))
y1=int(input("Enter y:"))

print("Point 2")
x2=int(input("Enter x:"))
y2=int(input("Enter y:"))

p1 = Point(x1,y1)
p2 = Point(x2,y2)

line = Polygon(p1,p2)
line.setOutline("red")
line.draw(win)

angle=int(input("Enter the angle of rotation"))
rotatedLine = rotateLine(line,angle)
rotatedLine.setOutline("cyan")
rotatedLine.draw(win)


win.getMouse()
win.close()