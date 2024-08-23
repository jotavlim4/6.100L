def sum_and_product(L):
    """
        L is a list of numbers
        returns a tuple where the first element is the sum of all numbers
        and the secondo is the product of all elements
    """
    sum, product = 0, 1
    for i in L:
        sum, product = (sum + i, product * i)
    return sum, product
    

my_list = [i for i in range(1, 6)]
print(sum_and_product(my_list))