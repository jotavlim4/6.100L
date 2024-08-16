# configurações iniciais
max_floor = 102
max_eggs = 7

# simulação de onde o ovo quebraria
highest_safety_floor = 102

# inicialização
low = 1
high = max_floor
num_guesses = 0 # num eggs
guess = (low + high) // 2

# bisection search
while num_guesses < max_eggs and low < high:
    num_guesses += 1
    print(f"Tentativa {num_guesses}: testando o andar {guess}")
    if guess > highest_safety_floor:
        print(f"O ovo quebrou no andar {guess}")
        high = guess - 1
    else:
        print(f"O ovo não quebrou no andar {guess}")
        low = guess
    guess = (low + high) // 2
print(f"O andar mais seguro é {guess}, encontrado em {num_guesses} tentativas")
