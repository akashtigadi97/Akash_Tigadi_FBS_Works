#WAP a programe to reverse three digit number

num = int(input('Enter a three digit number '))
temp = num

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10
reverse = (d1*100)+(d2*10)+d3

print(f'The reverse of {temp} is {reverse} ')