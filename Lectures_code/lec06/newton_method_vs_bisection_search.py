# initial setup bs
x = 2
epsilon = 0.00000000000001
low = 0
high = max(1, x)
mid = (low + high)/2
num_guesses = 0

#bisection search
while abs(mid**2 - x) >= epsilon:
    num_guesses += 1
    if mid**2 < x:
        low = mid
    else:
        high = mid
    mid = (high + low)/2

print(f"num iteration until a 'good enough' answer performing bisection search: {num_guesses}")
print(f"approximation for square root: {mid}\n")

# initial setup newton method
k = x
mid = k/2
num_guesses = 0

# newton method
while abs(mid**2 - k) >= epsilon:
    num_guesses += 1
    mid = mid - (((mid**2)-k)/(2*mid))
   
print(f"num iteration until a 'good enough' answer performing newton method: {num_guesses}")
print(f"approximation for square root: {mid}\n")