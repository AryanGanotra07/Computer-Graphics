from graphics import *
win = GraphWin("Test 1.1", 600, 600)
def ROUND(a):
    return int(a + 0.5)
def drawDDA(x1, y1, x2, y2):
    x,y = x1, y1
    length = abs((x2-x1) if abs(x2-x1) > abs(y2-y1) else (y2-y1))
    dx = (x2-x1)/float(length)
    dy = (y2-y1)/float(length)
    slope = (y2 - y1)/(x2-x1)
    if (slope < 0):
        print("Positive slope")
    elif slope >= 0:
        print("Negative slope")
    print("slope = ", slope)
    print("x = ", ROUND(x))
    print("y = ", ROUND(y))
    win.plotPixel(x,y,"red")
    for i in range(length):
        x += dx
        y += dy
        print("x = ", ROUND(x))
        print("y = ", ROUND(y))
        win.plotPixel(x,y,"red")

def main():
    x1 = int(input("Enter Start X: "))
    y1 = int(input("Enter Start Y: "))
    x2 = int(input("Enter End X: "))
    y2 = int(input("Enter End Y: "))

    drawDDA(x1, y1, x2, y2)
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()