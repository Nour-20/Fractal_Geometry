
# Python code for Mandelbrot Fractal

# Import necessary libraries
from PIL import Image
from numpy import complex, array
import numpy as np
import colorsys

# setting the width of the output image as 1024
WIDTH = 1000
# a function to return a tuple of colors
# as integer value of rgb


def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0+i/10, 0.5*i/100))
    return tuple(color.astype(int))

# function defining a mandelbrot


def mandelbrot(x, y):
    c0 = complex(x, y)
    c = 0
    for i in range(1, 1000):
        if abs(c) > 4:
            return rgb_conv(i*4)
        if abs(c) > 3:
            return rgb_conv(i*3)
        if abs(c) > 2:
            return rgb_conv(i)
        if (i+1) == 1000 and abs(c) < 1:
            return rgb_conv(i)
        if (i+1) == 1000 and abs(c) < 2 and abs(c) > 1:
            return rgb_conv(i/10+i)
        c = c*c + c0
    return (0, 0, 0)


# creating the new image in RGB mode
img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))
pixels = img.load()

for x in range(img.size[0]):

    # displaying the progress as percentage
    print("%.2f %%" % (x / WIDTH * 100.0))
    for y in range(img.size[1]):
        pixels[x, y] = mandelbrot((x - (0.75 * WIDTH)) / (WIDTH / 4),
                                  (y - (WIDTH / 4)) / (WIDTH / 4))

# to display the created fractal after
# completing the given number of iterations
img.show()
