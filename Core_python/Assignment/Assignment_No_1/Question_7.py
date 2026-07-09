# Write a programe to find the roots of a quadratic equation

import cmath

a = float(input('Enter a coefficient a: '))

b = float(input('Enter a coefficient b: '))

c = float(input('Enter a coefficient c: '))

# Calculate the discriminant

d = (b**2) - (4*a*c)

# Find the two roots

root1 = (-b - cmath.sqrt(d))/(2*a)

root2 = (-b - cmath.sqrt(d))/(2*a)

print('the root are {0} and {1}'.format(root1,root2))