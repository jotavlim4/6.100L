num = int(input("type a integer: "))
decimal_num = num
result = ''
if num < 0:
    is_neg = True
    num = abs(num)
else:
    is_neg = False
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num // 2
if is_neg:
    result = '-' + result
print(f"{str(decimal_num)}_(10) is equal to {result}_(2)")
