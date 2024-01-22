def summa(x, y):
   z = 0
   for number in range(x, y+1):
      z = z + number
   print("Сумма" , z)


x=int(input("Введіть початковє значення - "))
y=int(input("Введіть кінцеве значення - "))
if __name__ == '__main__':
   summa(x,y)



