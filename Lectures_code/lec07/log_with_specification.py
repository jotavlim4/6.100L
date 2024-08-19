def log(x: int | float, base: int, epsilon: int | float ):
    """
    Assumes x and epsilon int or float, base an int, x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon of x.
    """
    if x <= 1 or epsilon <= 0:
        return None
    lower_bound = 0
    while base**lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    ans = (low + high)/2
    while abs(base**ans - x) >= epsilon:
        if base**ans < x:
            low = ans
        else:
            high = ans
        ans = (low + high)/2
    if ans < 1:
        return None
    else:
        return ans

def test_log(x_vals, base=10, epsilon=0.001):
    for x in x_vals:
        result = log(x, base, epsilon)
        if result == None:
            print('Try another value!')
        else:
            print(f"result: {result}")
        
x_vals = (-1, 4, 8, 16, 32)
test_log(x_vals, base=2)