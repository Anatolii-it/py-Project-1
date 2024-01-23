from func import del_number



x = int(input("Ведідіть число яке потрібно знайти та видалити - "))
list1 = [1, 2, 3, 4, 5, 6, 7, 2, 9, 10]
if __name__ == '__main__':
    del_number(list1 , x)
    print("Число - ", x ,"Зустричалось ", del_number(list1,x) )

