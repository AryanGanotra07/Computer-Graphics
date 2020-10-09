import PIL.ImageDraw as ImageDraw,PIL.Image as Image, PIL.ImageShow as ImageShow 
im = Image.new('RGB', (680, 680)) 
#The 2 numbers are dimentions, pick what you want.
draw = ImageDraw.Draw(im)

draw.line((90,50,400,50))
#A
draw.arc((50,50,100,100), -140, 90)
draw.arc((50,100,100,150), -90, 140)
draw.line((70,100,120,100))
draw.line((70,100,120,100))
draw.line((120,50,120,150))
#R
draw.line((140,50,140,150))
draw.arc((150,50,200,120), 220, 450)
draw.line((170,120,220,150))
#YA
draw.arc((210,50,260,120), 220, 450)
#draw.arc((235,50,300,120), 90, 0)
draw.line((235,120,300,120))
draw.line((300,50,300,150))
#N
draw.line((400,50,400,150))
draw.line((320,100,400,100))
draw.arc((320,100,340,120), 0, 360)


im.show()