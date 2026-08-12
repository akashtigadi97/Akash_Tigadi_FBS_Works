#Write a program to create three lists of numbers, their squares and cubes

li = [1,2,3,4,5,6,7,8,9,10]
square_List =[]
Cube_List = []
for i in li:
    element = i ** 2
    square_List.append(element)
    element = i ** 3
    Cube_List.append(element)
print('Original list',li)
print('Square list',square_List)
print('Cube list',Cube_List)