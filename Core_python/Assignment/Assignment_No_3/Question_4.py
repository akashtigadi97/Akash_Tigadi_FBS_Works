#Write a program to input all sides of a triangle and check whether triangle is valid or not. 
number1 = int(input('Enter the number:'))
number2 = int(input('Enter the number:'))
number3 = int(input('Enter the number:'))

if (number1+number2>number3)and(number1+number3>number2)and(number2+number3>number1):
    print('The triangle is valid')
else:
    print('The triangle is Notvalid')