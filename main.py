def neparni_test(x, y):
   for number in range(1 + 1, 12):
      if number % 2 != 0:
         print(number,end=' ')

x=int(input("Введіть початковє значення"))
y=int(input("Введіть кінцеве значення"))
neparni_test(x,y)


