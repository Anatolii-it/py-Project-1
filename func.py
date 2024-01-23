def p_p_number(number):
    if number <= 1:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

def k_p_numbers(list):
    s = 0
    for number in list:
        if p_p_number(number):
            s += 1
    return s