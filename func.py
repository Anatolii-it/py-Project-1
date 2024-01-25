def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Факторіал від'ємного числа не існує"
    else:
        return n * factorial(n-1)

def c_factorials(numbers):
    factorials = [factorial(x) for x in numbers]
    return factorials


