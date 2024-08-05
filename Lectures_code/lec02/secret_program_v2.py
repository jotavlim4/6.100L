secret_number = 10
guess = int(input('Guess a integer: '))

answer = (secret_number == guess)

if answer:
    print("you're right!")
else:
    print("you're wrong!")
    if secret_number > guess:
        print('your guess is to loo!')
    else:
        print('your guess is too high!')
