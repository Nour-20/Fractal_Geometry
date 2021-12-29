# Python code for Tree Of Life

# Import necessary libraries
from math import cos, sin, pi
from PIL import Image, ImageDraw

# setting the width and the height of the output image
WIDTH = 1024
HEIGHT = 500


class Point:
    def __init__(self, x, y):
        self.x = round(x, 4)
        self.y = round(y, 4)

    def __str__(self):
        return f"Point is : {self.x}, {self.y}"


# Function drawing a line
def Draw(start, length, image, angle = pi/2):
    end = Point(cos(angle)*length + start.x,start.y - (sin(angle)*length))
    image.line([(start.x, start.y), (end.x, end.y)], fill='black', width=2)
    return end


# Recursive Function Tree
def Tree(start, length, levels, image, angle = pi/2):
    if levels == 0:
        return None
    else:
        # fork and length
        fork = pi/10
        length /= 2

        # Draw
        left_point=Draw(start, length, image, angle-fork) # left
        Tree(left_point, length, levels-1, image, angle-fork)

        right_point=Draw(start, length, image, angle+fork) # right
        Tree(right_point, length, levels-1, image, angle+fork)

        top_point = Draw(start, length, image, angle-fork/4) # top
        Tree(top_point, length, levels-1, image, angle-fork/4)

        top_point = Draw(start, length, image, angle+fork/4) # top
        Tree(top_point, length, levels-1, image, angle+fork/4)
        
        


# creating the new image in RGB mode
img = Image.new('RGB', (WIDTH, HEIGHT), color='white')
img1 = ImageDraw.Draw(img)

length = 400
level = 10

startPoint = Point(WIDTH/2, HEIGHT)
Tree(startPoint, length=length, levels=level, image=img1)

img.show()
