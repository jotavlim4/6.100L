def eval_quadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    Returns the value of the quadratic a×x² + b×x + c.
    """
    return a*(x**2) + b*x + c

def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    """
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    Evaluates one quadratic with coefficients a1, b1, c1, at x1.
    Evaluates another quadratic with coefficients a2, b2, c2, at x2.
    Prints the sum of the two evaluations. Does not return anything.
    """
    sum = (a1*(x1**2) + b1*x1 + c1) + (a2*(x2**2) + b2*x2 + c2)
    print(sum)

# print(eval_quadratic(1, 1, 1, 1)
two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1))
