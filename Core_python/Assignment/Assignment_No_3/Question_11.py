#Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
#  a. Children below 12 = 30% discount
#  b. Senior citizen (above 59) = 50% discount
#  c. Others need to pay full

age1 = int(input("Enter the first age:"))
tprice1 = float(input('Enter the tprice:'))
total_price=0

if age1 < 12:
    total_price = total_price + (tprice1 * 0.30)   
elif age1 < 59:
    total_price = total_price + (tprice1 * 0.50)   
else:
    total_price = total_price + tprice1 




age2 = int(input("Enter the sencond age:"))
tprice2 = float(input('Enter the tprice:'))


if age2 < 12:
    total_price = total_price + (tprice2 * 0.30)   
elif age2 < 59:
    total_price = total_price + (tprice2 * 0.50)   
else:
    total_price = total_price + tprice2 


age3 = int(input("Enter the third age:"))
tprice3 = float(input('Enter the tprice:'))


if age3 < 12:
    total_price = total_price + (tprice3 * 0.30)   
elif age3 < 59:
    total_price = total_price + (tprice3* 0.50)   
else:
    total_price = total_price + tprice3


age4 = int(input("Enter the fourth age:"))
tprice4 = float(input('Enter the tprice:'))


if age4 < 12:
    total_price = total_price + (tprice4 * 0.30)   
elif age4 < 59:
    total_price = total_price + (tprice4 * 0.50)   
else:
    total_price = total_price + tprice4 

age5 = int(input("Enter the five age:"))
tprice5 = float(input('Enter the tprice:'))


if age5 < 12:
    total_price = total_price + (tprice5 * 0.30)   
elif age5 < 59:
    total_price = total_price + (tprice5 * 0.50)   
else:
    total_price = total_price + tprice5 

print(f'Total of five person:',{total_price})

