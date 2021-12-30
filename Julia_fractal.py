
# Python code for Julia Set Fractal

# Import necessary libraries
from PIL import Image, ImageEnhance
from math import sqrt
import numpy as np
import colorsys
import random

# setting the width and the height of the output image 
WIDTH = 1280 
HEIGHT = 720
# a function to return a tuple of colors
# as integer value of rgb
def rgb(i):
    red = random.randint(i%2,i%256)
    green = random.randint(i%2,i%256)
    blue = random.randint(i%2,i%256)
    color = (red,green,blue)
    return color

def rgb_conv(i):
    color = 255 * np.array(colorsys.hsv_to_rgb(i/128,i/64,i/128))
    return tuple(color.astype(int))

# Function to scale the real part
def scale_real(real,width,r):
    x=((2*r)/width)*real-r
    return x
# Function to scale the imaginary part
def scale_img(image,height,r):
    y=((2*r)/height)*image-r
    return y

# Function defining a Julia Set
def julia(pixelx,pixely,x0,y0):

    c0=complex(x0, y0)
    R=(1+sqrt(1+(4*abs(c0))))/2+1 # escape radius

    zx=scale_real(pixelx,WIDTH,R)
    zy=scale_img(pixely,WIDTH/2,R)
    z = complex(zx,zy)

    i=0
    iter_max=1000
    while i<iter_max and abs(z)<(R**2):
        z = z**2 + c0
        i+=1
    
    if i == iter_max:
        return (0,0,0)
    else:
        return rgb(i)


def evaluateJulia(x0,y0):
    # creating the new image in RGB mode
    img = Image.new('RGB', (WIDTH, HEIGHT), color='blue')
    pixels = img.load()

    for pixelx in range(img.size[0]):

        # displaying the progress as percentage
        print("{:.2f} %".format(pixelx / WIDTH * 100.0))
        for pixely in range(img.size[1]):
            pixels[pixelx, pixely] = julia(pixelx,pixely,x0,y0)

    #image brightness enhancer
    enhancer = ImageEnhance.Contrast(img)

    factor = 3 #gives original image
    img = enhancer.enhance(factor)

    # to display the created fractal after
    # completing the given number of iterations
    img.save("julia.png")

if __name__ == '__main__':
    evaluateJulia(-0.835, -0.2321)
