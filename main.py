def my_minimum(list):
    number = int(my_list[0])
    for i in list:
        if i < number:
            number = i
    return number


my_list = [9, 2, 7, 4, 5]
rezultat = my_minimum(my_list)

if __name__ == '__main__':
    print("Сума елементів" ,rezultat)