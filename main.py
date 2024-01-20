def o_line(l, n, s):
   if napryam == "г":
      print(simvol * l)
   elif napryam == "в":
      for _ in range(l):
         print(simvol)
   else:
      print("Неправильний напрямок. Виберіть 'г - горизонтальний' або 'в - вертикальний'.")
l = int(input("Введіть довжину- "))
napryam = (input("Введіть напрямок в-вертикально г-горизонтально- "))
simvol = (input("Введіть символ яким малювати- "))

o_line(l, "n", "s")

