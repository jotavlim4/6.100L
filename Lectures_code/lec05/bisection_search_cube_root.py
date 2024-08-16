x = 27
abs_x = abs(x)
epsilon = 0.00000000000001
num_guesses, low = 0, 0
high = max(1, abs_x)
ans = (high + low)/2
while abs(ans**3 - abs_x) >= epsilon:
    print(f"low = {low}, high = {high}, ans = {ans}")
    num_guesses += 1
    if ans**3 < abs_x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2
if x < 0:
    ans = -ans
print(f"number of guesses = {num_guesses}")
print(f"{ans} is close to cube root of {x}")
