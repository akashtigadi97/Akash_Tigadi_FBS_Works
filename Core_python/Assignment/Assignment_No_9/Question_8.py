# Write a program to check whether a number is prime or not using recursion.

def Prime(num, i=2):
    if num<2:
        return False
    if i ==num:
        return True
    if num % i == 0:
        return False
    return Prime(num, i+1)
num =int(input('enter number:'))
if Prime(num):
    print('Prime number')
else:
    print('Not prime number')