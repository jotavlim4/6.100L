import math

NUM = 1000
count, low = 0, 0
high = 1000
answer = math.floor((high + low)/2)

while answer != NUM:
    count += 1
    if answer < NUM:
        low = answer + 1
    else:
        high = answer - 1
    answer = math.floor((high + low)/2)

print(f"count: {count}")
print(f"answer: {answer}")