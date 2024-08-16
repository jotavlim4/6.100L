x = 123456
epsilon = 0.01
step = epsilon**3
num_guesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans*ans <= x:
    ans += step
    num_guesses += 1
print("number of guesses =", num_guesses)
if abs(ans**2 - x) >= epsilon:
    print("failed on square root of", x)
else:
    print(ans, "is close to square root of", x)
