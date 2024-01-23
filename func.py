def del_number(my_list, x):
    k_dell = my_list.count(x)
    my_list = [i for i in my_list if i != x]
    return k_dell
