def biscetion_squared_root(x):
    """
    x is a float > 0
    return a approximation to square root of x with an epsilon precison
    """
    if x < 0:
        return None
    epsilon = 0.001
    low = 0
    high = max(1, x)
    best_guess = (low + high)/2.0
    while abs(best_guess**2 - x) >= epsilon:
        if best_guess**2 < x:
            low = best_guess
        else:
            high = best_guess
        best_guess = (low + high)/2.0
    return best_guess
    
def test_bisection_square_root(x_vals):
    for x in x_vals:
        if biscetion_squared_root(x) == None:
            print(f'square root of {x} do not in real set.')
        else:
            print(f"{biscetion_squared_root(x):.5f} is a good enough approximation for the squared root of {x:3d}")

# test = (i for i in range(1, 1000))
# test_bisection_square_root(test)

def count_nums_with_sqrt_close_to(n , epsilon):
    """
    n is an int > 2
    epsilon is a positive number < 1
    return how many integers have a squared root with epsilon of n
    """
    count = 0
    for i in range(n**3):
        sqrt = biscetion_squared_root(i)
        if abs(n - sqrt) < epsilon:
            count += 1
            print(f"sqrt({i:03d}) = {sqrt:10f} is close to {n}")
    return count
    
print(f"total: {count_nums_with_sqrt_close_to(10, 1)}")