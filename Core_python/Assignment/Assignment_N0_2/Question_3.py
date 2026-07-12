# WAP convert distant given in feet and inches into meter and centimeter

feet = int(input('Enter feet:'))

inches = int(input('Enter inches:'))

total_inches = (feet*12)+inches

meter = total_inches*0.0254

centemeter = meter*100

print(f'meter = {meter} and centimeter = {centemeter}')