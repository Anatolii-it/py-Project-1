
try:
   elements = input("Введить елементи списку цілих чисел через пробіл ").split()
   elements = [int(element) for element in elements]
   number_to_find = int(input("Введіть число для пошуку:"))
   count = elements.count(number_to_find)
   print(f"Число {number_to_find} знайдено {count} разів")


except Exception as e:
   print(e)


