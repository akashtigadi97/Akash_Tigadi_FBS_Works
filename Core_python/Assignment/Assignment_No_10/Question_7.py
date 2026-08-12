#WAP to create a new list from existing list which contain cube of each number of list 
li1= [1,2,3,4,5,6]
li2= []
for i in li1:
    num = i ** 3
    li2.append(num)
print(f'New cube list from existing list {li2}')