# WAP convert the time entered in hh,min and sec into second

hours = int(input('Enter hours:'))
minute = int(input('Enter minutes:'))
second = int(input('Enter second:'))

total_second = (hours*3600)+(minute*60)+second

print(f'total second is {total_second}')