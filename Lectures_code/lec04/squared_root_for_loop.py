# a guess and check solution using for loop with aim to verify if a x number is a perfect square:
# we can't have square root negative, soo we can add some code for that.

num = int(input("Type a integer: "))
neg = False
if num < 0:
    neg = True
for guess in range(0, abs(num)):
    if guess**2 >= num:
        break
    guess += 1

if guess**2 == num:
    print(f"{num} is a perfect square!")
else:
    print(f"{num} isn't a perfect square!")
    if neg:
        print(f"just checking... did you mean {-num}?")
