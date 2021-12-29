# Python program to print partial Koch Curve.
# importing the libraries : turtle standard 
# graphics library for python
from turtle import *
  
#function to create koch snowflake or koch curve
def snowflake(lengthSide, levels):
    if levels == 0:
        forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1)
    left(60)
    snowflake(lengthSide, levels-1)
    right(120)
    snowflake(lengthSide, levels-1)
    left(60)
    snowflake(lengthSide, levels-1)
    right(120)
  
# main function
if __name__ == "__main__":
  
    # defining the speed of the turtle
    speed(0)                   
    length = 600.0                   
  
    snowflake(length, 4)
  
    # To control the closing windows of the turtle
    mainloop() 