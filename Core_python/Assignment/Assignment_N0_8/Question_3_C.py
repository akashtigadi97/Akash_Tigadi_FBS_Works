#WAP to find of following series using function  
#1¹ + 2² + 3³ + ..... + nⁿ                                                

def SumPower(n):
    return sum(i**i for i in range(1,n+1))
n =int(input('Enter value of n:'))
sum1 = SumPower(n)
print(f'Sum of series c {sum1}')