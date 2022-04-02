# Python code for Sierpinski Carpet
from PIL import Image, ImageDraw

# setting the width and the height of the output image 
WIDTH = 1280
HEIGHT = 720

class Point:
    def __init__(self, x, y):
        self.x = round(x, 4)
        self.y = round(y, 4)


#Function drawing a square
def Draw_Square(p1,p2,p3,p4,fill,image):
    image.polygon([(p1.x,p1.y),(p2.x,p2.y),(p4.x,p4.y),(p3.x,p3.y)], fill =fill)


def get_square_points(point,length):
    """Point is on the top left corner of the square"""
    p1 = Point(point.x+length,point.y)
    p2 = Point(point.x,point.y+length)
    p3 = Point(point.x+length, point.y+length)
    return p1,p2,p3

def side_points(point,length):
    v1=Point(point.x+length/3,point.y)
    v2=Point(point.x+2*(length)/3,point.y)
    v3=Point(point.x,point.y+length/3)
    v4=Point(point.x,point.y+2*(length)/3)
    # v5=Point(point.x+length,point.y+length/3)
    # v6=Point(point.x+length,point.y+2*(length)/3)
    # v7=Point(point.x+length/3,point.y+length)
    # v8=Point(point.x+2*(length)/3,point.y+length)
    return v1,v2,v3,v4

def Sierp_Carp(point,length,levels,fill,image):

    if levels == 0:
        return None

    v1,v2,v3,v4=side_points(point,length)

    length=length/3

    p1= Point(v1.x,v1.y+length)

    p2,p3,p4=get_square_points(p1,length)

    Sierp_Carp(point=point,length=length,levels=levels-1,fill='black',image=image)
    Sierp_Carp(v1,length=length,levels=levels-1,fill='black',image=image)
    Sierp_Carp(v2,length=length,levels=levels-1,fill='black',image=image)
    Sierp_Carp(v3,length=length,levels=levels-1,fill='black',image=image)
    Sierp_Carp(v4,length=length,levels=levels-1,fill='black',image=image)
    Sierp_Carp(p2,length=length,levels=levels-1,fill='black',image=image)
    Sierp_Carp(p3,length=length,levels=levels-1,fill='black',image=image)
    Sierp_Carp(p4,length=length,levels=levels-1,fill='black',image=image)

    Draw_Square(p1,p2,p3,p4,fill='black',image=image)

img = Image.new('RGB', (WIDTH, HEIGHT))
img1 = ImageDraw.Draw(img)  

fill='white'
level = 4

square_length = 300
p1 = Point((WIDTH/2)-(square_length/2), (HEIGHT/2)-(square_length/2))
p2, p3, p4 = get_square_points(p1,square_length)

Draw_Square(p1,p2,p3,p4,fill,img1)
Sierp_Carp(p1,square_length,levels=level,fill=fill,image=img1)

img.show()