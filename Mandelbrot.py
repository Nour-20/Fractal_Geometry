# Python code for Mandelbrot Fractal

# Import necessary libraries
from PIL import Image, ImageEnhance
from PIL import Image
import numpy as np
import colorsys
import time
import os


# setting the width and height of the output image 
# 460 480
# 720 576
# 720 480
# 1280 720 
# 1440 1080 
# 1920 1080 
# 2048 1080
# 3840 2160
# 4096 2160

WIDTH = 1280 
HEIGHT = 720

# a function to return a tuple of colors
# as integer value of rgb


# def rgb(i):
#     red = int(i / 255.0)
#     green = int(1.0+i/10.0)
#     blue = int(0.5*i/100.0)
#     color = (red, green, blue)
#     return color


def rgb(i):
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 0.64, i/128.0))
    return tuple(color.astype(int))

# function defining a mandelbrot
def mandelbrot(x, y, dimension):
    c = complex(x, y)
    z = 0
    for i in range(1, 100):
        if abs(z) > 2:
            return rgb(i)
        # z =complex(abs(z.real),abs(z.imag)) #Burning ship
        z = z**dimension+ c
    return (0, 0, 0)

# Main function


def evaluateMandelbrot(dimension):
    # get the path to the current python file directory
    path = os.path.dirname(os.path.realpath(__file__))

    # creating the new image in RGB mode
    img = Image.new('RGB', (WIDTH, HEIGHT))
    pixels = img.load()

    start = time.time()
    for x in range(img.size[0]):

        # displaying the progress as percentage
        print("{:.2f} %".format(x / WIDTH * 100.0))

        for y in range(img.size[1]):
            pixels[x, y] = mandelbrot((x - (0.65 * WIDTH)) / (0.2*WIDTH),
                                      (y - (0.5*HEIGHT))/(0.3*HEIGHT), dimension)

    #image brightness enhancer
    enhancer = ImageEnhance.Contrast(img)

    factor = 10 #gives original image
    img = enhancer.enhance(factor)

    # to display the created fractal after
    # completing the given number of iterations
    img.save(path + "/mandelbrot.png")

    print("Done!")


if __name__ == '__main__':
    evaluateMandelbrot(2)
