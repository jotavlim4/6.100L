num = int(input('type a positive integer greater than 2: '))
smallest_divisor = None
for i in range(3, num):
    if num % i == 0:
        smallest_divisor = i
        break
if smallest_divisor != None:
    print(f'Smallest divisor of {num} is {smallest_divisor}')
else:
    print(f'{num} is a prime')
