# Python code for Tree Of Life 

# Import necessary libraries
import math
from PIL import Image, ImageDraw

# setting the width and the height of the output image 
WIDTH = 1024
HEIGHT = 1000

class Point:
    def __init__(self,x,y):
        self.x = round(x,4)
        self.y = round(y,4)

    def __str__(self):
        return f"Point is : {self.x}, {self.y}"


# Function drawing a line 
def Draw(start, end, image):
    image.line([(start.x,start.y),(end.x,end.y)], fill='black',width=5)
    

# Recursive Function Tree
def Tree(start,end,length,levels,image, angle = math.pi/2):
    if levels == 0:
        return None
    else:        
        length = 2*length/3

        # branch
        start = Point(end.x,end.y)
        end = Point(math.cos(angle)*length + start.x,start.y - (math.sin(angle)*length))

        # right
        Tree(start,end,length,levels-1,image,angle-math.pi/10)
        #left
        Tree(start,end,length,levels-1,image, angle+math.pi/10)

        Draw(start,end,image)



# creating the new image in RGB mode
img = Image.new('RGB', (WIDTH, HEIGHT), color='white')
img1 = ImageDraw.Draw(img)  

length = 200
level = 20

startPoint= Point(WIDTH/2,HEIGHT)
endPoint = Point(WIDTH/2,HEIGHT-200)
Tree(startPoint,endPoint,length=length,levels=level, image=img1)

img.show()