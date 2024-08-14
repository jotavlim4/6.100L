# a guess and check solution for find if a x number is a perfect square:
# we can't have square root negative, soo we can add some code for that.
guess = 0
neg = False
num = int(input("Enter a integer: "))
if num < 0:
    neg = True
while guess**2 < num:
    guess += 1
if guess**2 == num:
    print(f"{num} is a perfect square!")
else:
    print(f"{num} isn't a perfect square!")
    if neg:
        print(f"just checking... did you mean {-num}?")
