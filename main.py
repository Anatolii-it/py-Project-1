def is_prime(number):
    if number <= 1:
        print("false")
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print("false")
            return False
    print("True")
    return True

number = int(input("введіть число для перевірки чи є воно простим - "))
is_prime(number)
