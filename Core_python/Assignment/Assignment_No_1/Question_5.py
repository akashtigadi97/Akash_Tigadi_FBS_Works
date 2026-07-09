# Write a programe to enter P,T,R and calculate compound interest

P = float(input('Enter principle amount:'))

T = float(input('enter time in year:'))

R = float(input('Enter rate of interest:'))

Compound_Interest = P*(1 + R/100)** T-P

print('Compound interest is ',Compound_Interest)