x, y, z = 1, 2, 10
largest = -10000000

if (x % 2 != 0) or (y % 2 != 0) or (z % 2 != 0):
    if(largest < x and x % 2 != 0):
        largest = x
        print(f'{x} is max!')
    
    if(largest < y and y % 2 != 0):
        largest = y
        print(f'{y} is max!')
        
    if(largest < z and z % 2 != 0):
        largest = z
        print(f'{z} is max!')
else:
    if x < y and x < z:
        print(f'{x} is least!')
    elif y < z:
        print(f'{y} is least!')
    else:
        print(f'{z} is least!')