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
def Draw(start, end, image):
    image.line([(start.x, start.y), (end.x, end.y)], fill='black', width=5)


# Recursive Function Tree
def Tree(start, length, levels, image):
    if levels == 0:
        return None
    else:
        # wide angle and length
        angle = pi/3
        length /= 2

        # Get 3 branches of the tree
        top_point = Point(start.x, start.y - length)

        left_point = Point(start.x + sin(angle)*length,
                           start.y-cos(angle)*length)

        right_point = Point(start.x-sin(angle)*length,
                            start.y-cos(angle)*length)

        # Draw
        Draw(start, top_point, image)
        Draw(start, left_point, image)
        Draw(start, right_point, image)

        # recursion
        Tree(top_point, length, levels-1, image)
        Tree(left_point, length, levels-1, image)
        Tree(right_point, length, levels-1, image)


# creating the new image in RGB mode
img = Image.new('RGB', (WIDTH, HEIGHT), color='white')
img1 = ImageDraw.Draw(img)

length = 200
level = 5

startPoint = Point(WIDTH/2, HEIGHT)
Tree(startPoint, length=length, levels=level, image=img1)

img.show()
