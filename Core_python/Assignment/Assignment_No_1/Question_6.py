# Write a programe to input two angles frome user and fine third angle of triangle.

angle1 = int(input('Enter first angle of triangle:'))

angle2 = int(input('Enter second angle of triangle'))

angle3 = 180 - (angle1 + angle2)

print('Third angle of triangle is:',angle3)