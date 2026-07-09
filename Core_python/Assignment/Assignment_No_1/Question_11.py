# Write a programe to find the area and circumference of circle.

import math

radius = float(input('Enter the radius of the circle:'))

area = math.pi*radius**2

circumference = 2*math.pi*radius

print('area of the circle is:',area)

print('circumference of the circle is:',circumference)