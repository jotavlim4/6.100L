def sum_odd(a, b):
    """
    input: integers a and b
    output: returns the sum of all odd integers between a and b (inclusive)
    """
    sum = 0
    for i in range(a, b + 1):
        if i%2 != 0:
            sum += i
    return sum
    
print(sum_odd(2, 4))
print(sum_odd(2, 7))