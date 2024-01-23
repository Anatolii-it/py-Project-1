from func import p_p_number
from func import k_p_numbers



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = k_p_numbers(my_list)

if __name__ == '__main__':
    k_p_numbers(my_list)
    print("Кількість простих чисел - ", result)