sum = 0
for num in range(3, 1000, 2):
    is_prime = True
    for j in range(3, int(num ** 0.5) + 1, 2):
        if num % j == 0:
            is_prime = False
            break
    if is_prime:
        sum = sum + num
print(sum)
