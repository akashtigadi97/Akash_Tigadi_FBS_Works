#Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random

userid = input("Enter Userid: ")
password = input("Enter Password: ")

if userid == "akash" and password == "1234":
    captcha = random.randint(1000, 9999)
    print('Your captcha', captcha)

    user = int(input("Enter Captcha: "))

    if user == captcha:
        print("Login Successful")
    else:
        print("Captcha Incorrect")
else:
    print("Invalid User ID or Password")