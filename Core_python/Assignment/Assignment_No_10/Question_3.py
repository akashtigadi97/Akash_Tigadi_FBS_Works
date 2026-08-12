#WAP to find the second largest element in the list

li = [10,22,34,56,7,6,89,]

max = li[0]
for i in range(1,len(li)):
    if (li[i] > max):
        Second_Largest_Element = max
        max = li[i]
    elif(li[i] > Second_Largest_Element and li[i]):
        Second_Largest_Element = li[i]
print(f'The second largest element in list is {Second_Largest_Element}')