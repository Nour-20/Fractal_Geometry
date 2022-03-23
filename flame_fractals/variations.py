#Import modules
from math import sin, cos, atan2 , sqrt, pi, tan, exp, cosh, sinh, ceil
import random

# variation 0
def var_linear(x,y):
    return x,y
# variation 1
def var_sinusoidal(x,y):
    return sin(x),sin(y)
# variation 2
def var_spherical(x,y):
    r = sqrt(x**2+y**2)
    return x/r**2,y/r**2
# variation 3
def var_swirl(x,y):
    r = sqrt(x**2+y**2)
    return x*sin(r**2)-y*cos(r**2),x*cos(r**2)+y*sin(r**2)
# variation 4
def var_horseshoe(x,y):
    r = sqrt(x**2+y**2)
    return (x-y)*(x+y)/r , 2*x*y/r
# variation 5
def var_polar(x,y):
    r = sqrt(x**2+y**2)
    theta = atan2(y,x)
    return theta/pi, r-1
# variation 6
def var_handkerchief(x,y):
    r = sqrt(x**2+y**2)
    theta = atan2(y,x)
    return r*sin(theta+r), r*cos(theta-r)
# variation 7
def var_heart(x,y):
    r = sqrt(x**2+y**2)
    theta = atan2(y,x)
    return r*sin(theta*r), -r*cos(theta*r)
# variation 8
def var_disc(x,y):
    theta = atan2(y,x)
    r = sqrt(x**2+y**2)
    return (theta/pi)*sin(pi*r), (theta/pi)*cos(pi*r)
# variation 9
def var_spiral(x,y):
    r = sqrt(x**2+y**2)
    theta = atan2(y,x)
    x = cos(theta)+sin(r)
    y = sin(theta)-cos(r)
    return x/r,y/r
# variation 10
def var_hyperbolic(x,y):
    r = sqrt(x**2+y**2)
    theta = atan2(y,x)
    return sin(theta)/r , r*cos(theta)
# variation 11
def var_diamond(x,y):
    theta = atan2(y,x)
    r = sqrt(x**2+y**2)
    return sin(theta)*cos(r),cos(theta)*sin(r)
# variation 12
def var_ex(x,y):
    theta = atan2(y,x)
    r = sqrt(x**2+y**2)
    p0 = sin(theta+r)
    p1 = cos(theta-r)
    return r*(p0**3+p1**3), r*(p0**3-p1**3)
# variation 13
def var_julia(x,y):
    r = sqrt(sqrt(x**2+y**2))
    theta = atan2(y,x) *0.5
    if(random.randint(0,1)==1):
        theta += pi
    return r*cos(theta), r*sin(theta)
# variation 14
def var_bent(x,y):
    if(x>=0 and y>=0):
        return x,y
    elif (x<0 and y>=0):
        return 2*x,y
    elif (x>=0 and y<0):
        return x,y/2
    else:
        return 2*x,y/2
# variation 15
def var_waves(x,y,b,c,e,f):
    return x + b*sin(y/c**2), y + e*sin(x/f**2)
# variation 16
def var_fisheye(x,y):
    r = 2/(sqrt(x**2+y**2)+1)
    return r*y,r*x  
# variation 17
def var_popcorn(x,y,c,f):
    return x+c*sin(tan(3*y)), y+f*sin(tan(3*x))
# variation 18
def var_exponential(x,y):
    r = exp(x-1)
    return r*cos(pi*y), r*sin(pi*y)
# variation 19
def var_powers(x,y):
    r= sqrt(x**2+y**2)
    theta = atan2(y,x)
    r = r**sin(theta)
    return r*cos(theta), r*sin(theta)
# variation 20
def var_cosine(x,y):
    return cos(pi*x)*cosh(y), -sin(pi*x)*sinh(y)
# variation 21
def var_rings(x,y,c):
    r = sqrt(x**2+y**2)
    theta = atan2(y,x)
    r = (r+c**2)%(2*c**2)-c**2+r*(1-c**2)
    return r*cos(theta), r*sin(theta)
# variation 22
def var_fan(x,y,c,f):
    t = pi*c*c
    theta= atan2(y,x)
    r = sqrt(x**2+y**2)
    if((theta+f)%t > (t/2)):
        theta = theta - t/2
        return r*cos(theta), r*sin(theta)
    else:
        theta = theta + t/2
        return r*cos(theta), r*sin(theta)
# variation 23
def var_blob(x,y,p1,p2,p3):
    r = sqrt(x**2+y**2)
    theta = atan2(y,x)
    r = r*(p2+0.5*(p1-p2)*(sin(p3*theta)+1))
    return r*cos(theta), r*sin(theta)
# variation 24
def var_pdj(x,y,p1,p2,p3,p4):
    return sin(p1*y)-cos(p2*x),sin(p3*x)-cos(p4*y)
# variation 25
def var_fan2(x,y,p1,p2):
    theta = atan2(y,x)
    r = sqrt(x**2+y**2)
    t =theta + p2 - p1*(int(2*theta*p2/p1))
    if(t>p1/2):
        theta = theta-p1/2
        return r*sin(theta),r*cos(theta)
    else:
        theta = theta+p1/2
        return r*sin(theta),r*cos(theta)
# variation 26
def var_rings2(x,y,p1):
    r = sqrt(x**2+y**2)
    theta = atan2(y,x)
    t = r -2*p1*(int((r+p1)/(2*p))) + r*(1-p1)
    return t*sin(theta),t*cos(theta)
# variation 27
def var_eyefish(x,y):
    r = sqrt(x**2+y**2)
    r = 2/(r+1)
    return r*x,r*y
# variation 28
def var_bubble(x,y):
    r = sqrt(x**2+y**2)
    r = 4/(r*r+4)
    return r*x,r*y
# variation 29
def var_cylinder(x,y):
    return sin(x),y
# variation 30
def var_perspective(x,y,p1,p2):
    r = p2/(p2-y*sin(p1))
    return r*x,r*y*cos(p1)
# variation 31
def var_noise(x,y):
    ksi1 = random.random()
    ksi2 = random.random()
    return ksi1*x*cos(2*pi*ksi2), ksi1*y*sin(2*pi*ksi2)
# variation 32
def var_juliaN(x,y,p1,p2):
    ksi = random.random()
    p3 = int(abs(p1)*ksi)
    phi = atan2(x,y)
    t =  (phi+2*pi*p3)/p1
    r = sqrt(x**2+y**2)
    r = r**(p2/p1)
    return r*cos(t),r*sin(t)
# variation 33
def var_juliaScope(x,y,p1,p2):
    ksi = random.random()
    p3 = int(abs(p1)*ksi)
    tau = random.randint(0,1)
    phi = atan2(x,y)
    t = (tau*phi+2*pi*p3)/p1
    r= sqrt(x**2+y**2)
    r = r**(p2/p1)
    return r*cos(t), r*sin(t)
# variation 34
def var_blur(x,y):
    ksi1 = random.random()
    ksi2 = random.random()
    return ksi1*cos(2*pi*ksi2), ksi1*sin(2*pi*ksi2)
# variation 35
def var_gaussian(x,y):
    sum=0
    for i in range(4):
        ksi = random.random()
        sum+=ksi
    r = sum-2
    ksi = random.random()
    return r*cos(2*pi*ksi), r*sin(2*pi*ksi)
# variation 36
def var_ngon(x,y,p1,p2,p3,p4):
    phi = atan2(x,y)
    t = phi - p2*ceil(phi/p2)
    if(t>p2/2):
        t = t
    else:
        t=t-p2
    r = sqrt(x**2+y**2)
    k = (p3*(1/cos(t))-p3+p4)/(r**p1)
    return k*x, k*y
# variation 37
def var_curl(x,y,p1,p2):
    t1 = 1+p1*x+p2*(x*x-y*y)
    t2 = p1*y+2*p2*x*y
    r = 1/(t1*t1+t2*t2)
    return r*(x*t1+y*t2),r*(y*t1-x*t2)
# variation 38
def var_tangent(x,y):
    return sin(x)/cos(y), tan(y)
# variation 39
def var_cross(x,y):
    r = sqrt(x**2-y**2)
    r = 1/r*r
    r = sqrt(r)
    return r*x,r*y