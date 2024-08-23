# é uma função muito simples para 
# precisar de uma definição.
# podemos substituí-la por uma lambda funciton
def is_even(n):
    return n%2 == 0
    
def apply(criteria, n):
    """
        criteria is a function that takes in a number and returns a bool
        n is a int
        returns how many ints from 0 to n(inclusive) match the criteria
        (i.e. returns true when run with criteria)
    """
    count = 0
    for i in range(1, n+1):
        if criteria(i):
            count += 1
    return count

answer_with_lambda_function = apply((lambda x: x%2==0), 1000)
answer_without_lambda = apply(is_even, 1000)

print(answer_with_lambda_function)
print(answer_without_lambda)