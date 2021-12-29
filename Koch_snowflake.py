# Python code for Koch SnowFlakes Fractal
import sys
from PIL import Image, ImageDraw

# Constants
ERROR = 0.1
WIDTH = 1280
HEIGHT = 720

class Point:
    def __init__(self, x, y):
        self.x = round(x,4)
        self.y = round(y,4)

    def __str__(self):
        return f"{self.__class__.__name__} coordinates is : ({self.x}, {self.y})\n"


# Compute the midpoint coordinates


def computeMidPoint(point1, point2):
    midpoint = Point(((point1.x+point2.x)/2), ((point1.y+point2.y)/2))
    return midpoint

# Compute euclidean distance between two points


def computeDistance(point1, point2):
    return ((point1.x-point2.x)**2 + (point1.y-point2.y)**2)**0.5

# Get coefficients of the equation
# get a and b parameters in y = ax + b


def get_line_params(point1, point2):

    slope = ((point2.y-point1.y)/(point2.x-point1.x))
    b = (point1.y - slope*point1.x)

    if b - (point2.y - slope*point2.x) > ERROR:
        print(f"Error in {get_line_params}")
        sys.exit()

    return slope, b

# Solve the quadratic equation


def solve_quadratic_equation(A, B, C):
    delta = B**2 - 4*A*C
    if delta >= 0:
        solution1 = ((-B+(delta)**0.5)/(2*A))
        solution2 = ((-B-(delta)**0.5)/(2*A))
        return solution1, solution2
    else:
        print("Imaginery Solution in {solve_quadratic_equation}")
        sys.exit()
        

# Get point coordinates with respect to 2 another points


def getCoordinates(point1, point2, distance, place="inner"):
    
    # for vertical line (no slope)
    if point1.x==point2.x:
        y1 = point1.y+distance
        y2 = point1.y-distance
        x1 = point1.x
        x2 = point1.x

    # Other cases
    else:
        # get the line equation y=ax+b
        a, b = get_line_params(point1, point2)
        # compute coefficients of quadratic equation
        A=1
        B=-2*point1.x
        C=point1.x**2-(distance**2)/(a**2+1)

        # get point coordinates
        x1, x2 = solve_quadratic_equation(A, B, C)

        y1 = a*x1 + b
        y2 = a*x2 + b

    if place == 'inner':
        coordinates = min(Point(x1, y1), Point(x2, y2),
                          key=lambda x: computeDistance(x, point2))
        return coordinates
    elif place == 'outside':
        coordinates = max(Point(x1, y1), Point(x2, y2),
                          key=lambda x: computeDistance(x, point2))
        return coordinates
    else:
        print(f"Error : {place} take either 'outside' or 'inside' as input !")
        sys.exit()

# Koch snowflake algorithm


def koch_snowflake(vertex1, vertex2, vertex3, level, image):
    """ This function takes as arguments the coordinates of the 3 vertices of the triangle"""

    if level == 0:
        return None

    else:

        midpoint1 = computeMidPoint(vertex1, vertex2)
        midpoint2 = computeMidPoint(vertex2, vertex3)
        midpoint3 = computeMidPoint(vertex1, vertex3)

        # midpoint1 = getCoordinates(vertex1,vertex2, computeDistance(vertex1,vertex2)/2)
        # midpoint2 = getCoordinates(vertex2, vertex3, (computeDistance(vertex2, vertex3)/2))
        # midpoint3 = getCoordinates(vertex1, vertex3, (computeDistance(vertex1, vertex3)/2))
    
        # Compute the summits of the triangles
        #                   summit1
        #                      *
        #                    *   *
        #                  *       *
        #                *           *
        #  sidePoint12 * * * * * * * * * sidePoint21
        summit1 = getCoordinates(midpoint1, vertex3, (computeDistance(midpoint1, vertex3)/3), place="outside")
        summit2 = getCoordinates(midpoint2, vertex1, (computeDistance(midpoint2, vertex1)/3), place='outside')
        summit3 = getCoordinates(midpoint3, vertex2, (computeDistance(midpoint3, vertex2)/3), place='outside')
    
        # Compute triangles side points
        # 1----P------------2 : sidePoint12
        # 1-------------P---2 : sidePoint21
        # 2----P------------3 : sidePoint23
        # 2-------------P---3 : sidePoint32
        # 1----P------------3 : sidePoint13
        # 1-------------P---3 : sidePoint31
        sidePoint12 = getCoordinates(vertex1, vertex2, (computeDistance(vertex1, vertex2)/3))
        sidePoint21 = getCoordinates(vertex2, vertex1, (computeDistance(vertex1, vertex2)/3))
    
        sidePoint23 = getCoordinates(vertex2, vertex3, (computeDistance(vertex2, vertex3)/3))
        sidePoint32 = getCoordinates(vertex3, vertex2, (computeDistance(vertex3, vertex2)/3))
    
        sidePoint13 = getCoordinates(vertex1, vertex3, (computeDistance(vertex1, vertex3)/3))
        sidePoint31 = getCoordinates(vertex3, vertex1, (computeDistance(vertex3, vertex1)/3))
        

        # Draw a triangle
        image.polygon([(vertex1.x,vertex1.y), (vertex2.x,vertex2.y), (vertex3.x,vertex3.y)], fill = (255,0,0))

        # recursion
        koch_snowflake(summit1, sidePoint21, sidePoint12, level-1, image)
        koch_snowflake(summit2, sidePoint23, sidePoint32, level-1, image)
        koch_snowflake(summit3, sidePoint31, sidePoint13, level-1, image)
        koch_snowflake(vertex1, sidePoint12, sidePoint13, level-1, image)
        koch_snowflake(vertex2, sidePoint21, sidePoint23, level-1, image)
        koch_snowflake(vertex3, sidePoint32, sidePoint31, level-1, image)

p1 = Point((WIDTH/2)-400, (HEIGHT/2)+(200*(3**0.5)/3))
p2 = Point((WIDTH/2)+400, (HEIGHT/2)+(200*(3**0.5)/3))
p3 = Point((WIDTH/2), (HEIGHT/2)-(200*(3**0.5)))

# Create empty black canvas
im = Image.new('RGB', (WIDTH, HEIGHT), color='white')
# Draw red and yellow triangles on it and save
draw = ImageDraw.Draw(im)

koch_snowflake(p1, p2, p3, level=8, image=draw)

im.show()

