def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def c_factorials(numbers):
    factorials = int([factorial(x) for x in numbers])
    return factorials


