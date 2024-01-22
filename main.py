
def neparni(x, y):

   for zminna in range(x , y+1):
      if zminna % 2 != 0:
         print(zminna , end=" ")

   z = x = y = 0
x = int(input('Введіть початкове число - '))
y = int(input("Введіть кінцеве число - "))
if __name__ == '__main__':
   neparni(x,y)
   print("Непарні")