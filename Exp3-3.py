from graphics import *
win = GraphWin("Experiment 3.3", 600, 600)
import random

#text
label = Text(Point(290, 24), 'Draw a Ellipse')
label.setSize(24)
label.draw(win)
# oval = Oval(Point(100,50), Point(500,250))
# oval.draw(win)
#Oval
while True:
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    # oval1 = oval.clone()
    # oval1.move(x, 0)
    # oval.undraw()
    # oval1.undraw()
    
    # oval1.draw(win)
    # oval2 = oval.clone()
    # oval2.move(0, x)
    # oval2.draw(win)
    oval = Oval(Point(100+x,50+y), Point(500+x,250+y))
    oval.draw(win)
    time.sleep(1)
    oval.undraw()


win.getMouse()
win.close()