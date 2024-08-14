# itera diretamente sobre o indice da string:
s = 'joao victor'
for i in range(len(s)): # 0 t0 len(s)-1
    if s[i] == 'r' or s[i] == 'j':
        print("we're on begin or end of the string.")
        break

# os proximos loops iteram diretamente sobre a string.

s = 'ele é legal'
for char in s:
    if char == ' ':
        print('there is a space on the string')
        break

s = 'meu nome é joao victor lima da silva0'
for char in s:
    if char in '0123456789':
        print('there is numerical char on the string')
        break
