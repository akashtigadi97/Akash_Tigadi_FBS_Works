# Write a program to calculate the m to the power n using recursion.


def Power(m,n):
    if(n==0):
        return 1
    return m * Power(m,n-1)
m = int(input('Enter base:'))
n =int(input('Enter power:'))

print('Answer:',Power(m,n))