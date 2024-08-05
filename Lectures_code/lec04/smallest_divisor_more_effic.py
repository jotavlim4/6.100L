num = int(input('type a integer greater than 2: '))
smallest_divisor = None
if num % 2 == 0:
    smallest_divisor = 2
else:
    ## checa apenas números impares, pois se num nao é div por 2, então nenhum outro
    ## par divide num
    for i in range(3, num, 2):
        if num % i == 0:
            smallest_divisor = i
            break
if smallest_divisor != None:
    print(f'{smallest_divisor} is the smallest divisor os {num}')
else:
    print(f'{num} is prime!')
