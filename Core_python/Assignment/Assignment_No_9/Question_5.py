# Write a program to find factorial using recursion.

def Fatorial(num):
    if num == 0 or num == 1:
        return 1
    return num * Fatorial(num-1)
n = int(input('Enter the number:'))
result = Fatorial(n)
print(f' Factorial of {n} is {result}')