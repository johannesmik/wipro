def polyval(a, x):
    result = 0
    coefficients = len(a)
    for i in range(coefficients):
        result += a[i] * x ** i
    return result
