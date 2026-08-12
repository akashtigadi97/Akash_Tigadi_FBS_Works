# Write a program to find sum of digits using recursion.

def SumOfDigit(num):
    if num == 0:
        return 0
    return num % 10 + SumOfDigit(num // 10)

num = int(input('Enter number:'))
res = SumOfDigit(num)
print(f'Sum of digits in {num} number is {res}')