#WAP  find reverse of a number

def Reverse(num):
    rev  = 0
    while num > 0:
        d = num % 10
        rev = rev * 10+d
        num //= 10
    return rev
num = int(input('Enter the number:'))
res = Reverse(num)
print(f'The reverse number of {num} is {res}')