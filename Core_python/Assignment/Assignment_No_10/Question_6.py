#WAP to remove duplicate from list

li1 =[1,2,3,4,5,5,3,2,1]
li2 = []
for element in li1:
    if element not in li2:
        li2.append(element)
print(f'Original list',li1)
print(f'After removing duplicate items',li2)