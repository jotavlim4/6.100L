def bisection_solve(x, eval , epsilon, low, high):
    """
        x, epsilon, low and high are floats and power
        epsilon > 0, low <= high and there is an ans between low and high s. t.
        ans**power is within epsilon x
        returns ans s.t. ans**power within epsilon of x
    """
    ans = (low + high)/2
    while abs(eval(ans) - x) >= epsilon:
        if eval(ans) < x :
            low = ans
        else:
            high = ans
        ans = (low + high)/2
    return ans

def log(x, base, epsilon):
    if x < 0:
        return None
    def find_log_bounds(x, base):
        lower_bound = 0
        while base**lower_bound < x:
            lower_bound += 1
        return lower_bound - 1, lower_bound + 1
    low, high = find_log_bounds(x, base)
    return bisection_solve(x, lambda ans: base**ans, epsilon, low, high)

def test_log(x_vals, base=2, epsilon=0.000001):
    for x in x_vals:
        result = log(x, base, epsilon)
        if result == None:
            print('Try another value!')
        else:
            print(f"result: {result}")
        
x_vals = (-1, 4, 8, 16, 32)
test_log(x_vals)