# Import necessary libraries
from PIL import Image, ImageEnhance
from PIL import Image
from math import log
import sys
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

WIDTH = 720
HEIGHT = 480
MAX_LAMBDA = sys.maxsize
MIN_LAMBDA = -sys.maxsize

def rgb(i):
    red =0
    green=0
    blue=0
    if(i > 0):
        green = 120
        blue =  250
    elif(i<0):
        i = abs(i)
        red = 255-int(i*255/pow(i,1.48))
        green = 255-int(i*255/pow(i,1.3))
        blue = 255-int(i*255/pow(i,1.1))
    color = (red,green,blue)
    return color


def scale_px(a):
    a = a*(4)/WIDTH
    a = a+0.01 
    return a


def scale_py(b):
    b = b*(4)/HEIGHT
    b = b +0.01
    return b


# function defining a Lyapunov
def Lyapunov(a, b, sequence, N):
    deriv = 1
    sum_deriv = 0  # lambda

    r = 0
    x = 0.5

    a = scale_px(a)
    b = scale_py(b)

    for i in range(N):
        for char in sequence:
            if(char == 'a'):
                r = a
            else:
                r = b
            x = r*x*(1-x)
            deriv *= abs(r*(1-2*x))

        if(deriv < 0.0001):
            deriv = 0.0001

        sum_deriv += log(deriv)

    if(sum_deriv > MAX_LAMBDA):
        sum_deriv /= MAX_LAMBDA
    if(sum_deriv < MIN_LAMBDA):
        sum_deriv /= MIN_LAMBDA

    return rgb(sum_deriv/N)


# Main function
def evaluateLyapunov(sequence, max_iteration=50):
    # get the path to the current python file directory
    path = os.path.dirname(os.path.realpath(__file__))

    # creating the new image in RGB mode
    img = Image.new('RGB', (WIDTH, HEIGHT))
    pixels = img.load()

    for x in range(img.size[0]):
        # displaying the progress as percentage
        print("{:.2f} %".format(x / WIDTH * 100.0))
        for y in range(img.size[1]):
            pixels[x, y] = Lyapunov(
                x, y, sequence.strip().lower(), max_iteration)

    #image brightness enhancer
    enhancer = ImageEnhance.Contrast(img)

    factor = 10  # gives original image
    img = enhancer.enhance(factor)

    # to display the created fractal after
    # completing the given number of iterations
    img.save(path + "/Lyapunov.png")

    print("Done!")


if __name__ == '__main__':

    sequence = "bbbbaaaa"
    # max_iteration = 80
    evaluateLyapunov(sequence)
