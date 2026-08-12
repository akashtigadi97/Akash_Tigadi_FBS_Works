#Write a program to remove all occurrences of a given element in the list.

li = [10,20,30,30,45,67,45,60]
print('Original list occurences:',li)
num = int(input('Enter the element to remove completely:'))
Filtered_List = []
for i in li:
    if i !=num:
        Filtered_List.append(i)

print('List after removing occurences:',Filtered_List)