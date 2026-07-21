#Input 5 subject marks from user and display grade(eg.First class,Second class ..) 

sub1 = int(input('Enter the marks:'))
sub2 = int(input('Enter the marks:'))
sub3 = int(input('Enter the marks:'))
sub4 = int(input('Enter the marks:'))
sub5 = int(input('Enter the marks:'))

total_grade = sub1+sub2+sub3+sub4+sub5
percentage = (total_grade/500)*100
print(percentage)

if percentage > 85 and percentage <= 100:
    print("First Class")
elif percentage > 75:
    print("Second Class")
elif percentage > 65:
    print("Third Class")
elif percentage > 50:
    print("Fourth Class")
else:
    print("Fail")


