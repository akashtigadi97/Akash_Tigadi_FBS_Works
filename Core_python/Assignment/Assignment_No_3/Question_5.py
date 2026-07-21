#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle

a = int(input('Enter the number:'))
b = int(input('Enter the number:'))
c = int(input('Enter the number:'))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
