#WAP to create a duplicate of an existing list . It should not point to same list

Original_List = [10,20,30,40,50]
Duplicate_list = []
for element in Original_List:
    Duplicate_list.append(element)
Duplicate_list[0] = 100
print('Original list (Unchanged)',Original_List)
print('Duplicate list (Modified)',Duplicate_list)