#Write a program to input angles of a triangle and check whether triangle is valid or not.

number1 = int(input('Enter the number:'))
number2 = int(input('Enter the number:'))
number3 = int(input('Enter the number:'))

if number1+number2+number3 == 180:
    print('The triangle is valid')
else:
    print('The triangle is Notvalid')