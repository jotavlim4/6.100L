def find_root(x, power, epsilon):
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

# root = find_root(8, 3, 0.01)
# print(root)
