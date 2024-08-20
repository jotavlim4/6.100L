def calc(op, x, y):
    return op(x, y)
    
def div(a, b):
    if b != 0:
        return a/b
    print('Denom was 0.')
    
result = calc(div, 5, 0)
print(result)