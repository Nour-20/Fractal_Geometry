# Python code for T-Square Fractal
from PIL import Image, ImageDraw
import os

# Constants
WIDTH = 1280
HEIGHT = 720

class Point:
    def __init__(self, x, y):
        self.x = round(x, 4)
        self.y = round(y, 4)
    def __str__(self):
        return f"{self.__class__.__name__} coordinates is : ({self.x}, {self.y})\n"

#Function drawing a square
def Draw_Square(p1,p2,p3,p4,fill,image):
    image.polygon([(p1.x,p1.y),(p2.x,p2.y),(p4.x,p4.y),(p3.x,p3.y)], fill =fill)

def get_square_points(point,length):
    """Point is on the top left corner of the square"""
    p1 = Point(point.x+length,point.y)
    p2 = Point(point.x,point.y+length)
    p3 = Point(point.x+length, point.y+length)
    return p1,p2,p3

def top_left(point,length):
    p1=Point(point.x-length/2,point.y-length/2)
    return p1

def T_Square(point,length,levels,fill,image):
    
    if levels == 0:
        return None

    p2, p3, p4 = get_square_points(point,length)

    length = length/2

    v1=top_left(point,length)
    v2=top_left(p2,length)
    v3=top_left(p3,length)
    v4=top_left(p4,length)

    T_Square(v1,length=length,levels=levels-1,fill='white',image=image)
    T_Square(v2,length=length,levels=levels-1,fill='white',image=image)
    T_Square(v3,length=length,levels=levels-1,fill='white',image=image)
    T_Square(v4,length=length,levels=levels-1,fill='white',image=image)    
  
    Draw_Square(point,p2,p3,p4,fill,image)



def evaluateTSqu(level):
    # get path of the current python file directory
    path= os.path.dirname(os.path.realpath(__file__))
    # creating the new image in RGB mode
    img = Image.new('RGB', (WIDTH, HEIGHT))
    img1 = ImageDraw.Draw(img)  

    fill='white'

    square_length = 300
    p1 = Point((WIDTH/2)-(square_length/2), (HEIGHT/2)-(square_length/2))
    T_Square(p1,square_length,levels=level,fill=fill,image=img1)

    img.save(path + "/t_square.png")
    print("Done!")

if __name__ == '__main__':
    evaluateTSqu(6)

