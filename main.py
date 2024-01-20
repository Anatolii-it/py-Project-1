try:
   s= 0
   input_str = input("Введіть числа через пробіл - ")
   numbers = list(map(int,input_str.split()))
   for num in numbers:
      if s < num:
         s = num
   print("Найбільше - " ,s )
except Exception as e:
   print(e)

