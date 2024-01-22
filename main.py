def my_dob(list):
    dobutok = 1
    for i in list:
        dobutok *= i
    return dobutok


my_list = [1, 2, 3, 4, 5]
rezultat = my_dob(my_list)

if __name__ == '__main__':
    print("Сума елементів" ,rezultat)