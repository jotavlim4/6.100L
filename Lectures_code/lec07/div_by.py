def div_by(n, d):
    """
    input: n and d are positive integers
    output: true if d divides n and false otherwise 
    """
    return n % d == 0
    
print(div_by(10, 3))
print(div_by(195, 13))