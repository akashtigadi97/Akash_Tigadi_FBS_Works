#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)


gender = input('Enter the gender(m/f):')
age = int(input('Enter the age:'))

if gender=='f':
    if age>=18:
        print('Female are eligible for marry')
    else:
        print('Female are Noteligible for marry')
else:
    if age>=21:
        print('Male are eligible for marry')
    else:
        print('Male are Noteligible for marry')