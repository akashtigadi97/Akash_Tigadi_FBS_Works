#WAP to print Armstrong number within a given range

start = int(input('Enter starting number:'))
end = int(input('Enter ending number:'))

for num in range(start, end + 1):
    temp = num
    dig = len(str(num))
    total = 0

    while temp>0:
        digits = temp % 10
        total += digits ** dig
        temp //= 10

    if num == total:
        print(num)