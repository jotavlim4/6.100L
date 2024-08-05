'''
Assume you are given a positive integer variable named N.
Write a piece of Python code that finds the cube root of N.
The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube.
Hint: use a loop that increments a counter—you decide when the counter should stop.
'''
num = int(input('type a integer: '))
ans = 0
while ans**3 < abs(num):
    ans += 1

if ans**3 == abs(num):
    if num < 0:
        ans = -ans
    print(f'{num} is a perfect cube')
else:
    print('Error!')
