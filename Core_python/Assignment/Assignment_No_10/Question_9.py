#Write a program of having n number of elements in the list and find out even
#and odd elements in that list and then create two separate lists which will have
#even elements and other will have odd elements.

n =int(input('Enter the number:'))
li = []
for i in range(n):
    element = int(input('Enter element {i+1}:'))
    li.append(element)
Even_List = []
Odd_List = []
count = 0
for element in li:
    if element % 2 == 0:
        Even_List.append(element)
        count += 1
    else:
        Odd_List.append(element)
        count += 1
print('Total even element in list :',Even_List)
print('Total odd element in list :',Odd_List)