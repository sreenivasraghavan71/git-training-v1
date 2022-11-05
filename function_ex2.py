# Use some functions and values from the math module
from math import sqrt, sin, cos, pi, radians
print('When promted to enter the values of x and y; chose the x-value between 5000 to 10000 for the first position')
print('When promted to enter the values of x and y; chose the y-value as 0 for the first position')
print('Similarly chose the other position values as between 10000 and 20000 and y value as 0 again')
# Get coordinates of the stationary spacecraft, (px, py)
px = float(input("Enter x coordinate of spacecraft: "))
py = float(input("Enter y coordinate of spacecraft: "))
# Get starting coordinates of satellite, (x1, y1)
x = float(input("Enter initial satellite x coordinate: "))
y = float(input("Enter initial satellite y coordinate: "))
# Convert 60 degrees to radians to be able to use the trigonometric functions
rads = radians(60)
# Precompute the cosine and sine of the angle
COS_theta = cos(rads)
SIN_theta = sin(rads)
# Make a complete revolution (6*60 = 360 degrees)
for increment in range(0, 7):
# Compute the distance to the satellite
    dist = sqrt((px - x)*(px - x) + (py - y)*(py - y))
    print('Distance to satellite {0:10.2f} km'.format(dist))
# Compute the satellite's new (x, y) location after rotating by 60 degrees
    x, y = x*COS_theta - y*SIN_theta, x*SIN_theta + y*COS_theta

print(" The program run successfully and there are no error.")
print(" The program run successfully and there are no error1.")
print(" The program run successfully and there are no error2.")
print(" The program run successfully and there are no error3.")