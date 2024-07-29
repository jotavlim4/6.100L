# <expression> if <condition> else <expresion>
# funciona com operador ternário (?)

x, y, z = 1, 2, 3
max = (x if x > z else z) if (x > y) else (y if y > z else z)

print(max)