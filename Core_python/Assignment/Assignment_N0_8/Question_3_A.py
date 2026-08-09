#WAP to find of following series using function  
# 1 + 2 + 3 + 4 + ..... + n


def SumSeries(n):
    return sum(range(1,n+1))

n =int(input('Enter the number:'))
sum1 = SumSeries(n)
print(f'Sum of series is {sum1}')