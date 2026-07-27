#Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.


student = int(input('Enter number of student:'))

total_percentage = 0

for i in range(student):
    print('\nstudent',i+1)

    total =0
    for j in range(5):
        marks = float(input(f'Enter marks of subject {j+1}:'))
        total = marks

        percentage = total / 5
        print('percentage:',percentage)

        total_percentage += percentage

average = total_percentage / student
print('\nAverage percentage of student :',average)