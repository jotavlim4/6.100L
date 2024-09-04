def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    sum = 0
    for i in range(len(tA)):
        sum += tA[i] * tB[i]
    return len(tA), sum
    

tuple_1 = [2*i + 1 for i in range(3)]
tuple_2 = [3*i for i in range(3)]

print(dot_product(tuple_1, tuple_2))

