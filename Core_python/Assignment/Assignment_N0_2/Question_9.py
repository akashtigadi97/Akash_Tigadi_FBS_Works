#WAP to swap two numbers without using third variable

m = int(input('Enter first number:'))
n = int(input('Enter second number:'))

print(f'Before swapping : m = {m} and n = {n}')

m = m+n
n = m-n
m = m-n

print(f'After swapping : m = {m} and n = {n}')