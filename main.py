print('домашне завдання')
print('Виберіть літеру завдання ? а,б,в,г,д,е,ж,з,и,к')
operation = input()
i = j = 0
x=y=int(input('введіть сторону квадрату нечетне бажано: '))
if operation == 'а':
   while i < y:
      j = 0
      while j < x:
         if i <= int(y):
            if (i < j+1 and i < y+1 - j) or (i < j+1 and i > y  - j):
               print(f'[{i},{j}]', end=' ')
            else:
               print(f'     ', end=' ')
         j += 1
      print()
      i += 1
elif operation == 'б':
   while i < y:
      j = 0
      while j < x:
         if i <= int(y):
            if (i > j-1 and i < y  - j) or (i > j-1 and i > y - 1 - j):
               print(f'[{i},{j}]', end=' ')
            else:
               print(f'     ', end=' ')
         j += 1
      print()
      i += 1
elif operation == 'в':
   while i < y:
      j = 0
      while j < x:
         if i <= int(y):
            if i < j+1 and i < y  - j:
               print(f'[{i},{j}]', end=' ')
            else:
               print(f'     ', end=' ')
         j += 1
      print()
      i += 1
elif operation == 'г':
   while i < y:
      j = 0
      while j < x:
         if i <= int(y):
            if i > j-1 and i > y -1 - j - 1:
               print(f'[{i},{j}]', end=' ')
            else:
               print(f'     ', end=' ')
         j += 1
      print()
      i += 1
elif operation == 'д':
   while i < y:
      j = 0
      while j < x:
         if i <= int(y):
            if (i > j and i > y - 1 - j) or (i < j and i < y - 1 - j):
               print(f'[{i},{j}]', end=' ')
            else:
               print(f'     ', end=' ')
         j += 1
      print()
      i += 1
elif operation == 'е':
   while i < y:
      j = 0
      while j < x:
         if i <= int(y):
            if (i >= j and i <= y -1 - j) or (i <= j and i >= y - 1 - j):
               print(f' * ', end=' ')
            else:
               print(f'   ', end=' ')
         j += 1
      print()
      i += 1
elif operation == 'ж':
   while i < y:
      j = 0
      while j < x:
         if i <= int(y):
            if i >= j and i <= y - 1 - j:
               print(f' * ', end=' ')
            else:
               print(f'   ', end=' ')
         j += 1
      print()
      i += 1
elif operation == 'з':
   while i < y:
      j = 0
      while j < x:
         if i <= int(y):
            if i <= j and i >= y - 1 - j:
               print(f' * ', end=' ')
            else:
               print(f'   ', end=' ')
         j += 1
      print()
      i += 1
elif operation == 'и':
   while i < y:
      j = 0
      while j < x:
         if i <= int(y):
            if (i <= j and i <= y - 1 - j) or (i >= j and i <= y - 1 - j):
               print(f' * ', end=' ')
            else:
               print(f'   ', end=' ')
         j += 1
      print()
      i += 1
elif operation == 'к':
   wall = x - 1
   counter = 0
   while i < y:
      j = 0
      if i < int(y):
         counter += 1
      while j < x:
         # print(f'[{i},{j}]', end=' ')
         if i <= int(y):
            if (i >= j - 1 and i >= y - 1 - j) or (i <= j and i >= y - 1 - j):
               print(f' * ', end=' ')
            else:
               print(f'   ', end=' ')

         j += 1
      print()
      i += 1
elif operation == '':
   print(a * b)
else:
   print('Неизвестная операция')


