
# Python code for Sierpinski triangle

# Import necessary libraries
from PIL import Image, ImageDraw 

# setting the width and the height of the output image 
WIDTH = 1440
HEIGHT = 1080

#Function defining the midpoint coordinates
def mid(Point1, Point2):
    mid=((Point1[0]+Point2[0])/2,(Point1[1]+Point2[1])/2)
    return mid

#Function drawing a triangle
def Draw_Triang(p1,p2,p3,fill,image):
    image.polygon([p1,p2,p3], fill =fill, outline ="blue")

# Recursive Sierpenski Triangle Function
def Sierp(p1,p2,p3,fill,levels,image):
    if (levels==0):
        return None
    else:

        m1=mid(p1,p2)
        m2=mid(p1,p3)
        m3=mid(p2,p3)

        Draw_Triang(m1,m2,m3,fill,image)

        Sierp(p1,m1,m2,fill='white',levels=levels-1,image=image)
        Sierp(p2,m1,m3,fill='white',levels=levels-1,image=image)
        Sierp(p3,m2,m3,fill='white',levels=levels-1,image=image)



# creating the new image in RGB mode
img = Image.new('RGB', (WIDTH, HEIGHT))
img1 = ImageDraw.Draw(img)  

fill='blue'
level = 8

point1 = (WIDTH/4,HEIGHT/1.2)
point2 = (3*WIDTH/4,HEIGHT/1.2)
point3 = (WIDTH/2,HEIGHT/8)

Draw_Triang(point1,point2,point3,fill,image=img1)

Sierp(point1,point2,point3,fill=fill,levels=level, image=img1)

img.show()