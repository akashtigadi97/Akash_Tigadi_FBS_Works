#Write a program to check if user has entered correct userid and password

userid = (input('Enter userid:'))
password = int(input('Enter password:'))

if userid == 'akash'and password == '1234':
    print('Login succesfully')
else:
    print('Wrong userid and password')