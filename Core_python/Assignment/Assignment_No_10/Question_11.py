#Write a program to print all numbers which are divisible by m and n in the list.

li = [12,3,22,45,33,66,55,88,45]
m = int(input('Enter value of m to divide :'))
n = int(input('Enter value of n to divide :'))

for i in li:
    if(i % m ==0) and (i % n ==0):
        print(i,end=' ')
print()