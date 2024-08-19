def find_root(x: float, power: int, epsilon: float):
    if x < 0 and power%2 == 0:
        return None
    low = min(-1, x)
    high = max(1, x)
    ans = (low + high)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (low + high)/2
    return ans
    
def test_find_roots(x_val: float, powers: int, epsilons: float):
    for x in x_val:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                if result == None:
                    val = "No roots exists"
                else:
                    val = "Okay"
                    if abs(result**p - x) > e:
                        val = "Bad"
                print(f"if x = {x:9.3f}, power = {p:1d}, epsilon = {e:5.3f}, then val: {val:20} ")
                
x_vals = (0.25, 8, -8)
powers = (1, 2, 3)
epsilons = (0.1, 0.01, 0.001)
test_find_roots(x_vals, powers, epsilons)