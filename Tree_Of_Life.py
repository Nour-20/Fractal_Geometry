
# Python code for Tree Of Life 

# Import necessary libraries
import math
from PIL import Image, ImageDraw

# setting the width and the height of the output image 
WIDTH = 1024
HEIGHT = 500

class Point:
    def __init__(self,x,y):
        self.x = round(x,4)
        self.y = round(y,4)

    def __str__(self):
        return f"Point is : {self.x}, {self.y}"


# Function drawing a line 
def Draw(start, end, image):
    # start[0]-->x start
    # start[1]-->y start
    # end[0]-->x end
    # end[1]-->y end
    image.line([(start.x,start.y),(end.x,end.y)])
    

# Recursive Function Tree
def Tree(start,end,length,levels,image):
    if levels == 0:
        return None
    else:
        Draw(start,end,image)
        
        angle = math.pi/6

        # Right branch
        start_right = Point(end.x,end.y)
        end_right = Point(math.cos(angle)*length/2 + start_right.x,start_right.y - (math.sin(angle)*length/2))

        Tree(start_right,end_right,length/2,levels-1,image)

        # Left branch   
        start_left = Point(end.x,end.y)
        end_left = Point(-math.cos(angle)*length/2 + start_left.x,start_left.y - (math.sin(angle)*length/2 ))

        Tree(start_left,end_left,length/2,levels-1,image)



# creating the new image in RGB mode
img = Image.new('RGB', (WIDTH, HEIGHT))
img1 = ImageDraw.Draw(img)  

length = 200
level = 8

startPoint= Point(WIDTH/2,HEIGHT)
endPoint = Point(WIDTH/2,HEIGHT-200)
Tree(startPoint,endPoint,length=length,levels=level, image=img1)

img.show()