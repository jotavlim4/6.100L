x = int(input('type a integer: '))
count = 1
factorial = 1
while count <= x:
    factorial = factorial * count
    count = count + 1
print(f'{factorial} is the factorial of {x}')
