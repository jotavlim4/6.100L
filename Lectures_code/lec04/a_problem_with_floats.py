x = 0.0
for i in range(10):
    x += 0.1
if 1.0  - x < 0.0000000001:
    print(x,'= 1.0')
else:
    print(x, 'is not 1.0')
