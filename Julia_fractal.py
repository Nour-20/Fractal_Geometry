
# Python code for Julia Set Fractal

# Import necessary libraries
from PIL import Image, ImageEnhance
import numpy as np
import colorsys
import random

# setting the width and the height of the output image 
WIDTH = 1024
HEIGHT = 500
# a function to return a tuple of colors
# as integer value of rgb
def rgb(i):
    red = random.randint(i%2,i%256)
    green = random.randint(i%2,i%128)
    blue = random.randint(i%2,i%256)
    color = (red,green,blue)
    return color

def rgb_conv(i):
    color = 255 * np.array(colorsys.hsv_to_rgb(i/128,i/255,i/128))
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
def julia(x,y):
    c0=complex( -0.7269,0.1889)
    R=abs(c0)+1
    cx=scale_real(x,WIDTH,R)
    cy=scale_img(y,WIDTH/2,R)
    i=0
    iter_max=1000
    while i<iter_max and cx**2+cy**2<R**2:
        ctemp= cx**2 - cy**2
        cy=2*cx*cy + c0.imag
        cx= ctemp + c0.real
        i+=1
    
    if i==iter_max:
        return (0,0,255)
    else:
        return rgb(i)



# creating the new image in RGB mode
img = Image.new('RGB', (WIDTH, HEIGHT))
pixels = img.load()

for x in range(img.size[0]):

    # displaying the progress as percentage
    print("{:.2f} %".format(x / WIDTH * 100.0))
    for y in range(img.size[1]):
        pixels[x, y] = julia(x,y)

#image brightness enhancer
enhancer = ImageEnhance.Contrast(img)

factor = 3 #gives original image
img = enhancer.enhance(factor)

# to display the created fractal after
# completing the given number of iterations
img.show()
