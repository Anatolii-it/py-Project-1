def my_sum(list):
    summa = 0
    for i in list:
        summa += i
    return summa


my_list = [1, 2, 3, 4, 5]
rezultat = my_sum(my_list)

if __name__ == '__main__':
    print("Сума елементів" ,rezultat)