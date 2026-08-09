#  WAP to calculate area of circle

def AreaOfCircle(radius):
    return 3.14 * (radius ** 2)

r = float(input('Enter radius:'))

print('Area of circle is :',AreaOfCircle(r))