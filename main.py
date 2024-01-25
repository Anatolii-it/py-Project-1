from func import c_factorials

numbers = [3, 4, 5, 6]

if __name__ == '__main__':
    c_factorials(numbers)
    result = c_factorials(numbers)
    print("Список до змін     - ",numbers)
    print("Список факторіалів - ",result)
