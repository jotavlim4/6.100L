# p(x) = x^2 - 24
# p'(x) = 2x

k = 27
epsilon = 0.001
guess = k/2
count = 0
while abs(guess**3 - k) > epsilon:
    count += 1
    guess = guess - (((guess**3) - k)/(3*(guess**2)))
print(f"count: {count}")
print(f"square root of {k} is above {guess}")