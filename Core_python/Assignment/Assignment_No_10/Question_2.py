#WAP to find maximum and minimum element in a list

li = [10,20,30,40,50,555]
max = li[0]
min = li[0]
for i in range(1,len(li)):
    if (li[i] > max):
        max = li[i]
    elif(li[i] < min):
        min = li[i]
print(f'Maximum element in a list {max}')
print(f'Minimum element in a list {min}')