import sys
sys.setrecursionlimit(1500000)


import PIL.ImageDraw as ImageDraw,PIL.Image as Image, PIL.ImageShow as ImageShow 
im = Image.new('RGB', (400, 400)) 
draw = ImageDraw.Draw(im)

def boundary(x, y, new_col, boundary_col):
    if ((im.getpixel((x, y)) != boundary_col) and (im.getpixel((x, y)) != new_col)):
        print(im.getpixel((x, y)),new_col)
        im.putpixel((x,y), new_col)
        boundary(x + 1, y, new_col, boundary_col)
        boundary(x, y + 1, new_col, boundary_col)
        boundary(x-1, y, new_col, boundary_col)
        boundary(x, y - 1, new_col, boundary_col)

x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
x2=int(input("Enter x2:"))
y2=int(input("Enter y2:"))
rec=draw.rectangle((x1,y1,x2,y2),outline=(220,0,0))

x=90
y=100
fill = (0, 180, 10)
b_color=(220,0,0)
print(im.getpixel((x, y)))

boundary(x, y, fill, b_color)




im.show()