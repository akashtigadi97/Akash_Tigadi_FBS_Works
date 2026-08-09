#WAP to check if given number is armstrong number or not . For each task create separate function

def CountDigit(num):
    count = 0
    temp = num
    while temp>0:
        count +=1
        temp //= 10
    return count


# Function to check armstrong number

def IsArmstrong(num):
    digit_count = CountDigit(num)
    temp = num
    total = 0
    while temp>0:
        digit = temp % 10
        total += digit ** digit_count
        temp //= 10
    return total == num
num = int(input('Enter the number:'))
if IsArmstrong(num):
    print(num,' is an armstrong.')
else:
    print(num,'is an not armstrong.')