#WAP to accept an integer amount from user and tell minimum number of notes needed for representing that amount

amount = int(input('Enter amount:'))

n500 = amount//500
amount = amount%500

n200 = amount//200
amount = amount%200

n100 = amount//100
amount = amount%100

n50 = amount//50
amount = amount%50

n20 = amount//20
amount = amount%20

n10 = amount//10
amount = amount%10


print(f' 500 notes = {n500}')

print(f' 200 notes = {n200}')

print(f' n100 notes = {n100}')

print(f' n50 notes = {n50}')

print(f' n20 notes = {n20} ')

print(f' n10 notes = {n10} ')

print('remaining amount ',amount)
