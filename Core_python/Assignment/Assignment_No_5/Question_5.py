#Write a program to print prime numbers between 1 to 100.


print('prime number from 1 to 100:')

for i in range (1,101):
    if i>1:
        for j in range(2,int(i ** 0.5)+1):
            if(i % j)==0:
                break
        else:
            print(i,end=' ')