# Python code for Mandelbrot Fractal

# Import necessary libraries
from PIL import Image
import numpy as np
import colorsys
import time
import os
import sys


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
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 0.85, i/12.0))
    return tuple(color.astype(int))

# function defining a mandelbrot
def mandelbrot(x, y, d):
    c0 = complex(x, y)
    c = 0
    for i in range(1, 1000):
        if abs(c) > 2:
            return rgb(i)
        c = c**d + c0
    return (0, 0, 0)

# Main function


def main(img_number, path):
    # creating the new image in RGB mode
    img = Image.new('RGB', (WIDTH, HEIGHT))
    pixels = img.load()

    start = time.time()
    for x in range(img.size[0]):

        # displaying the progress as percentage
        print("{:.2f} %".format(x / WIDTH * 100.0))

        for y in range(img.size[1]):
            pixels[x, y] = mandelbrot((x - (0.65 * WIDTH)) / (0.2*WIDTH),
                                      (y - (0.5*HEIGHT))/(0.3*HEIGHT), (1/24)*img_number)

    # to save and display the created fractal after
    # completing the given number of iterations

    if(sys.platform in ['linux', 'linux2']):
        # Save image for linux system
        if(img_number < 10):
            img.save(path + "/Images/Mandelbrot/"+"im_00{}.jpg".format(img_number))
        elif (img_number < 100):
            img.save(path + "/Images/Mandelbrot/"+"im_0{}.jpg".format(img_number))
        else:
            img.save(path + "/Images/Mandelbrot/"+"im_{}.jpg".format(img_number))
    if(sys.platform in ['win32', 'cygwin', 'msys']):
        # Save image for window system
        if(img_number < 10):
            img.save(path+"\Images\Mandelbrot\im_00{}.jpg".format(img_number))
        elif(img_number < 100):
            img.save(path+"\Images\Mandelbrot\im_0{}.jpg".format(img_number))
        else:
            img.save(path+"\Images\Mandelbrot\im_{}.jpg".format(img_number))

    end = time.time()
    print("time is ", end-start)


if __name__ == '__main__':

    # get the path to the current python file directory
    path = os.path.dirname(os.path.realpath(__file__))

    # Frame count
    start_frame = 2*24
    end_frame = 3*24

    for img_number in range(start_frame,end_frame):
        main(img_number, path)
