# Write a program to print list after removing even numbers.

li = [2,33,44,5,54,66,80,98,100]
Removed_List = []

for i in li:
    if i % 2 != 0:
        Removed_List.append(i)

print('Original list',li)
print('List after removing even number from original list',Removed_List)
