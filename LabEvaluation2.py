import time
from graphics import *
def trafficLights():
    win = GraphWin()
    rect = Rectangle(Point(60,20 ), Point(140,180))
    rect.draw(win)
    red = Circle(Point(100, 50), 20)
    red.setFill("black")
    red.draw(win)
    yellow = Circle(Point(100, 100), 20)
    yellow.setFill("black")
    yellow.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    
    color = "red"
    lights = [ red, yellow, green ]
    while True:
        for i in range(len(lights)) :
            light = lights[i]
            light.setFill(color)
            for l in lights:
                if l!=light:
                    l.setFill("black")
            # not sure what the update function for the screen is but you need to call it before you call time.sleep()
            time.sleep(5)
            if color == "red":
                color = "yellow"
            elif color == "yellow":
                color = "green"
            elif color == "green":
                color = "red"
    win.getMouse()
trafficLights()

    