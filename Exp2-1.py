
from graphics import *
win = GraphWin("Experiment 2-1", 600, 600)
#text
label = Text(Point(250, 7), 'Plot pixels of different colors')
label.draw(win)
#plotPixels
win.plotPixel(150,150, "blue")
win.plotPixel(120,180, "red")
win.plotPixel(200,250, "black")
win.plotPixel(100,300, "green")
win.plotPixel(500,450, "orange")
win.plotPixel(150,520, "pink")
win.getMouse()
win.close()