# divide o código de find_root em multiplas funções com 
# a finalidade de tornar o código mais modularizado e objetivo.

def find_bound(x: float , power: int):
    """
        x a float and power a positive int
        returns low, high suct that low**power <= x and high**power >= x
    """
    low = min(-1, x)
    high = max(1, x)
    return low, high
    
def bisection_solve(x: float, power: int, epsilon: float, low: float, high: float):
    """
        x, epsilon, low and high are floats and power
        epsilon > 0, low <= high and there is an ans between low and high s. t.
        ans**power is within epsilon x
        returns ans s.t. ans**power within epsilon of x
    """
    ans = (low + high)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (low + high)/2
    return ans
    
def find_root(x: int | float, power: int, epsilon: int | float = 0.001):
    """
        assumes x ans epsilon int or float, power an int, epsilon > 0 and power >= 1
        returns float such that y**power is within epsilon of x
        if such that float does not exist, returns None
    """
    if x < 0 and power%2 == 0:
        return None
    low, high = find_bound(x, power)
    return bisection_solve(x, power, epsilon, low, high)
    
answer = find_root(27, 3)
print(answer)