def my_dob(list):
    dobutok = 1
    for i in list:
        dobutok *= i
    print("Добуток елементів - " , dobutok)


my_list = [9, 2, 7, 4, 5]

if __name__ == '__main__':
    my_dob(my_list)
