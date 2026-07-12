#WAP to swap two number using third variable

m = int(input('Enter first number:'))
n = int(input('Enter second number:'))

t = m
m = n
n = t

print(f'After swapping : first number {m} and second number {t}')