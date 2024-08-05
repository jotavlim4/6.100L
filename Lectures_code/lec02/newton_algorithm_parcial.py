## queremos descobrir qual o valor de
## g**3 = x, dado um x qualquer
## ou seja, qual o valor de g que ao cubo é
## igual a x.

x = float(input('Valor de x para encontramor a raiz cúbica: '))
g = float(input('Qual é o seu chute: ')) ## valor 'chutado'
print(f'cubo atual = {g**3}') ## o cubo do valor 'chutado'

next_g = g - ((g**3-x)/(3*g**2)) ## sugestão de próximo chute

## o proximo chute é = chute - f(chute)/f'(chute).
## esse é uma parte do método de newto para aproximações.

print(f'Próximo chute para tentar: {next_g}')
