from graphics import *
win = GraphWin("Translate Rectangle", 600, 600)

print("Corner 1")
x1=int(input("Enter x"))
y1=int(input("Enter y"))
c1=Point(x1, y1)

print("Corner 2")
x2=int(input("Enter x"))
y2=int(input("Enter y"))
c2 = Point(x2, y2)

r = Rectangle(c1, c2)
r.draw(win)

dx=int(input("Translation tx"))
dy=int(input("Translation ty"))

x1+=dx
x2+=dx
y1+=dy
y2+=dy

c1 = Point(x1,y1)
c2 = Point(x2, y2)
rt=Rectangle(c1, c2)
rt.draw(win)

win.getMouse()
win.close()