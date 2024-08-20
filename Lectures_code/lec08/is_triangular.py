def is_triangular(n):
    """
    n is an int > 0
    return true if n is triangular, i.e. equals a continued
    summation of natural numbers (1 + 2 + 3 + 4 + ... + k), false otherwise
    """
    total = 0
    for i in range(n+1):
        total += i
        if total == n:
            return True
    return False
        
def test_triangular(numbers):
    for n in numbers:
        if is_triangular(n):
            print(f'{n} is triangular')
        else:
            print(f"{n} isn't triangular")
            
numbers = (i for i in range(1, 1001))
test_triangular(numbers)