# WAP find the sum of three digit number

num = int(input('Enter a three digit number:'))

temp = num

d1 = num%10
num = num//10

d2 = num%10
num = num//10

d3 = num%10
num = num//10

sum_digit = d1+d2+d3

print(f'the sum of {temp} is {sum_digit}')