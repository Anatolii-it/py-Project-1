try:
   text = """Перш ніж переходити до вивчення цих різноманітних методів, необхідно розглянути особливості роботи
з рядками, а саме індексацію рядків. Оскільки рядок є ?
впорядкованим набором символів (є послідовністю),9
кожен елемент рядка (символ рядка) має свій унікальний 2 56
індекс (порядковий номер). Нумерація індексів починається з нуля. Індекс другого елемента рядка — 1 і так
далі. Індекс останнього символу визначається як довжина
рядка мінус один ?
   """
   c=z=y=x=0
   filter_text = str(text.lower())
   work1 = filter_text.title()
   print(work1)
   while x < 10:
      s = str(x)
      res = filter_text.count(s)
      x = x + 1
      if res == 1:
            y = y + 1
   print("цифр у тексті", y)
   list_words = filter_text.split()
   for word in list_words:
      if "," in word or "." in word:
         z = z + 1
   print("знаків припинання" , z)
   for word in list_words:
      if '?' in word:
         c = c + 1
   print("знаків оклику", c)
except Exception as e:
   print(e)