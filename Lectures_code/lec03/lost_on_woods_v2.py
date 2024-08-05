where = None
count = 0
while (where == 'right' or where is None):
    where = input('You are in the Lost Florest. Go left or go right? ')
    count = count + 1

    if count > 2:
        print(':(')

print('You got out!')
