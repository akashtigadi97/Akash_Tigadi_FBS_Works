# Write a program to prompt user to enter userid and password. If Id and  password is incorrect give him chance to re-enter the credentials. Let him try 3  times. After that program to terminate.  


user = 'akash'
pass1='@123'

for i in range(4):
    userid = input('Enter userid:')
    password = input('Enter password:')

    if userid == user and password == pass1:
         print('Login succesfully')
         break
    else:
        print('wrong userid and password')
        remaining = 3-i
        print('Incorrect credential remaining attempts:',remaining)


else:
    print('programe terminate because of too many attempts')
              
