def do_twice(n, f):
    return f(f(n))
    
print(do_twice(3, lambda x: x**2))