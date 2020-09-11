from graphics import *
win = GraphWin("Experiment 2-2", 600, 600)

#title
label = Text(Point(290, 7), 'Concentric Circles')
label.draw(win)

#center
center = Point(300, 300)

#circle1
c1 = Circle(center, 70)
c1.draw(win)

#circle2
c2 = Circle(center, 40)
c2.draw(win)

win.getMouse()
win.close()