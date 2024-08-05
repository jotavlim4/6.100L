num = int(input('Enter a integer greater than 2: '))
smallest_divisor = None
for i in range(2, num):
    if num % i == 0:
        smallest_divisor = i
        break
if smallest_divisor != None:
    largest_divisor = num // smallest_divisor
    print(f'smallest divisor of {num} is {smallest_divisor}')
    print(f'largest divisor of {num} is {largest_divisor}')
else:
    print(f'{num} is prime!')
