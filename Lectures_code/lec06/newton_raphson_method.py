# p(x) = x^2 - 24
# p'(x) = 2x

k = 3
epsilon = 0.001
guess = k/2
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
print(f"square root of {k} is above {guess}")