#WAP sum of all prime number between 1 to n

def IsPrime(num):
    if num<2:
        return False
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True
def SumOfPrime(n):
    total = 0
    for i in range(2,n+1):
        if IsPrime(i):
            total +=i
    return total
n = int(input('Enter the value of n:'))
res = SumOfPrime(n)
print(f'Sum of all prime number between 1 to {n} is {res} ')