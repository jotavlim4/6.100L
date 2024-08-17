NUM = 30
count, low, high = 0, 0, 24
while low <= high:
    count += 1
    answer = (low + high) // 2 # arredonda para baixo
    
    if answer < NUM:
        low = answer + 1 # precisamos excluir do próximo intervalo de busca o número já verificado 
    elif answer > NUM:
        high = answer - 1 # precisamos excluir do próximo intervalo de busca o número já verificado
    else:
        break
print(f"count: {count}")
print(f"answer: {answer}")