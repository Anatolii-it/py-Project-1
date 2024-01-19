try:
   s=c=e= 0
   input_str = input("Введіть числа через пробіл - ")
   numbers = list(map(int,input_str.split()))
   for num in numbers:
      s += num
      c = c + 1
   e = int(s/c)
   print("Сума дорівнює" ,s , "Середньоаріфметичне" , e)
except Exception as e:
   print(e)