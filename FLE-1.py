from graphics import *
win = GraphWin("Scale Triangle", 1200, 1200)
        
x1=int(input("Enter x"))
y1=int(input("Enter y"))
c1=Point(x1, y1)

print("Point 2")
x2=int(input("Enter x"))
y2=int(input("Enter y"))
c2 = Point(x2, y2)

print("Point 3")
x3=int(input("Enter x"))
y3=int(input("Enter y"))
c3 = Point(x3, y3)

P = [[x1,y1], [x2,y2], [x3,y3]]

b = Polygon(Point(P[0][0], P[0][1]), Point(P[1][0], P[1][1]), Point(P[2][0], P[2][1]))
b.setOutline('black')
b.draw(win)

rx=int(input("Enter fixed x:"))
ry=int(input("Enter fixed y:"))

sx=float(input("Enter scaling x:"))
sy=float(input("Enter scaling y:"))

S = [sx,sy]

for i in range(3):
    x_shifted = P[i][0]-rx 
    y_shifted = P[i][1]-ry
    print(P[i][0],P[i][1])
    P[i][0] = rx + (x_shifted*S[0]); 
    P[i][1] = ry + (y_shifted*S[1]);
    print(P[i][0],P[i][1])

b = Polygon(Point(P[0][0], P[0][1]), Point(P[1][0], P[1][1]), Point(P[2][0], P[2][1]))
b.setOutline('blue')
b.draw(win) 

win.getMouse()
win.close()