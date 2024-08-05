x = int(input('type a integer: '))
factorial = 1
for i in range(1, x + 1):
    factorial = factorial * i
print(f'{x}! = {factorial}')
