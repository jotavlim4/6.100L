x = int(input('type a int: '))
ans = 0
for num_interation in range(abs(x)):
    ans = ans + abs(x) ## abs -> funcão módulo, retorna o valor absoluto
print(f'({x})*({x}) = {ans}')
