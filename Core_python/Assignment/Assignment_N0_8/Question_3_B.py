#WAP to find of following series using function  
#1! + 2! + 3! + 4! + ..... + n!

import math
def SumFactorial(n):
   
         return sum(math.factorial(i) for i in range(1,n+1))
        
n = int(input('Enter value of n:'))
sum1 = SumFactorial(n)
print(f'Sum of series b {sum1}')

