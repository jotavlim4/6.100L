NUM = 987
count, low, high = 0, 0, 1000
while low <= high:
    count += 1
    answer = (low + high) // 2 # arredonda para baixo
    
    if answer < NUM:
        low = answer + 1
    elif answer > NUM:
        high = answer - 1
    else:
        break
print(f"count: {count}")
print(f"answer: {answer}")