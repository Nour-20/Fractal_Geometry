# Create a video clip from images provided in a folder
import cv2
import os
import sys

#grab last 3 characters of the file name:
def file_sort(x):
    return(x[-7:-4])

# get the path to the current python file directory
path = os.path.dirname(os.path.realpath(__file__))

# Image settings
# Path
if(sys.platform in ['linux', 'linux2']):
    # linux system
    image_folder = path+'/Images/Mandelbrot/'
if(sys.platform in ['win32', 'cygwin', 'msys']):
    # window system
    image_folder = path + "\Images\Mandelbrot\\"
# Extension
extension = ".jpg"
# Read images into list
images = [img for img in sorted(os.listdir(
    image_folder),key= file_sort) if img.endswith(extension)]


"""TODO check if images is empty"""
# Video settings
video_name = image_folder+'mandelbrot.mp4'
frame = cv2.imread(os.path.join(image_folder, images[0]))
# data
height, width, number_of_channels = frame.shape
codec = cv2.VideoWriter_fourcc(*'mp4v')  # Video coding
video = cv2.VideoWriter(video_name, codec, 8, (width, height))

print("Starting Video Creation.....")
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

print("Video Created!!")