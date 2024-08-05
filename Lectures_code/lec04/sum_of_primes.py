sum = 0
for num in range(3, 1000, 2):
    is_prime = True
    for i in range(3, int(num**(0.5)) + 1, 2):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        sum = sum + num
print(f'the sum of the prime numbers greater than 2 and less than 1000 is {sum}')
