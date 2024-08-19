x1 = 49
if x1 < 0:
    print("Does not exist!")
else:
    epsilon = 0.01
    low = 0
    high = max(1, x1)
    guess = (low + high)/2
    while abs(guess**2 - x1) >= epsilon:
        if guess**2 < x1:
            low = guess
        else:
            high = guess
        guess = (high + low)/2
x1_root = guess
x2 = -8
if x2 < 0:
    is_pos = False
    x2 = -x2
else:
    is_pos = True
low = 0
high = max(1, x2)
guess = (low + high)/2
while abs(guess**3 - x2) >= epsilon:
    if guess**3 < x2:
        low = guess
    else:
        high = guess
    guess = (low + high)/2

if is_pos:
    x2_root = guess
else:
    x2_root = -guess
    x2 = -x2
print(f"sum of square root of {x1} and cube root of {x2} is clote to {x1_root + x2_root}")
