from graphics import *
win = GraphWin()

#point and line
pt = Point(100,50)
line = Line(pt, Point(50, 100))
line.draw(win)

#circle
pt = Point(150, 100)
c = Circle(pt, 25)
c.draw(win)

#square
rect = Rectangle(Point(10, 10), Point(50,50))
rect.draw(win)

#rectangle
rect = Rectangle(Point(130, 140), Point(190,180))
rect.draw(win)

#text
label = Text(Point(100, 7), 'Experiment 1')
label.draw(win)


win.getMouse()
win.close()