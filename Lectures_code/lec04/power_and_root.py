num = int(input('type a integer: '))
found = False
for pwr in range(2, 6):
    root = round(abs(num)**(1/pwr))
    if root**pwr == num:
        print(f'{num} can be express by {root}^{pwr}')
        found = True
        #break
    elif (-root)**pwr == num:
        print(f'{num} can be express by {-root}^{pwr}')
        found = True
        #break
if not found:
    print("No such pair of integers (r, p) exists where 1 < p < 6 and r^p equals the entered integer.")
