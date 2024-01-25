from func import c_factorials

numbers = [3, 4, 5, 6]
result = c_factorials(numbers)
print("факторіал",result)  # Виведе: [6, 24, 120, 720]

if __name__ == '__main__':
    c_factorials(numbers)
    print(result)