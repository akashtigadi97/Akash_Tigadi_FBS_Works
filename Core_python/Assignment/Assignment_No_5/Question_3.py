# Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition : 
#a. Children below 12 = 30% discount 
#b. Senior citizen (above 59) = 50% discount 
#c. Others need to pay full. 


passenger = int(input('Enter number of passengers:'))
ticket = float(input('Enter ticket price:'))

total = 0

for i in range(passenger):
    age =int(input('Enter age of passenger:'))


    if age<12:
        price = ticket - (ticket * 0.30)
    elif(age > 59):
        price = ticket - (ticket * 0.50)
    else:
        price = ticket

    total+=price

print('Total price: ',total)
