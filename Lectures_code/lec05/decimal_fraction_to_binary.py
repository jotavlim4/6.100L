x = 13454.31
p = 0
# loop while para encontrar o valor de 'p' que faz (2^p)*x
# um número inteiro, ou seja, 'p' vai ser iterado enquanto
# (2^p)*x não deixar resto zero.
while (2**p)*x % 1 != 0:
    print(f"remainder = {str((2**p)*x - int((2**p)*x))}")
    p += 1
# convertemos esse número para int, com a finalidade de retirar o .0
num = int((2**p)*x)

# agora executamos o algoritmo para converter um número inteiro em número decimal
result = ''
if num == 0:
    result = '0'
else:
    while num > 0:
        result = str(num%2) + result
        num //= 2

# acrescenta os zeros a frente do número baseada no left/right shift
for i in range(p - len(result)):
    result = '0' + result
result = result[0:-p] + '.' + result[-p:]
print(f"the binary representatio of {x} is {result}")
