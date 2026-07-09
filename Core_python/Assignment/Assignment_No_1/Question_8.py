# Write a programe to convert days into years,weeks,and days.

days = int(input('Enter the number of days: '))

years = days//365

weeks = days//7

remaining_days = days%7

print('years',years)

print('weeks',weeks)

print('remaining_days',remaining_days)