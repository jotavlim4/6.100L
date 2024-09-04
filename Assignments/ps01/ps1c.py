## 6.100L PSet 1: Part C
## Name: João Victor


##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input('Enter the initial deposit: '))
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
COST_OF_DREAM_HOME = 800000.0
PORTION_DOWN_PAYMENT = .25
DOWN_PAYMENT = PORTION_DOWN_PAYMENT * COST_OF_DREAM_HOME
MONTHS = 36
EPSILON = 0.0001

def savings_amount(time, initial_deposit, r):
    savings = initial_deposit
    for i in range(time):
        savings += savings*(r/12)
    return savings

low = 0.0
high = 1.0
r = (low + high)/2
steps = 0
savings = savings_amount(MONTHS, initial_deposit, r)

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if initial_deposit >= DOWN_PAYMENT - 100:
    r = 0.0
elif initial_deposit*(1 + 1/12)**MONTHS < DOWN_PAYMENT - 100:
    r = None
else:
    while abs(savings - DOWN_PAYMENT) >= 100:
        steps += 1
        savings = savings_amount(MONTHS, initial_deposit, r)
        if savings < DOWN_PAYMENT:
            low = r
        else:
            high = r
        r = (low + high)/2


print(f'Best savings rate: {r} [or very close to this number]')
print(f'Steps in bisection search: {steps} [or very close to this number]')
