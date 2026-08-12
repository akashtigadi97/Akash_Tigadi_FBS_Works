# 10. Write a program to reverse a number using recursion.

def Reverse(n,rev=0):
    if(n == 0):
        return rev
    rev = rev * 10 + n % 10
    return Reverse(n // 10,rev)

n = int(input('Enter the number:'))
print('Reverse:',Reverse(n))