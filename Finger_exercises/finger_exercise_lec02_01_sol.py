x, y, z = 3, 41, 22
least = min(x, y, z) #guarda o menor valor entre x, y e z em 'least'

# testa se o menor valor é também impar
# se passar por todos esses if's testando falso para cada um deles
# vai printar o menor valor entre x, y, z

# se entrar em pelo menos um deles, vai printar o maior valor entre x, y e z\
# que também é impar

if x % 2 != 0:
    least = x
if y % 2 != 0 and least < y:
    least = y
if z % 2 != 0 and least < z:
    least = z
print(least)