count_nums = 0
largest = None ## inicializamos com None para poder fazer as comparações que precisamos
while (count_nums < 10):
    num = int(input('type a int: '))
    if (num % 2 != 0 and (largest == None or largest < num))
        largest = num
    count_nums = count_nums + 1
if largest == None:
    print('no odd number was typed!')
else:
    print(f'{largest} is the largest odd number!')
