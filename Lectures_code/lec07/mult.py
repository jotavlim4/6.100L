# modo 1:
def mult(num1: int, num2=1):
    return num1*num2
    
print('Modo 1:')
print(mult(20))
print(mult(20, 10), end='\n\n')


# mode 2, número variável de argumentos:
def mult_v2(*numbers):
    product = 1
    for n in numbers:
        product *= n
    return product

print('Modo 2:')
print(mult_v2(20))
print(mult_v2(20, 10))

