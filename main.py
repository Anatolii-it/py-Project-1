
print('калькулятор')
print('Виберіть дію на додатковій клавіатурі ? \n-, +, / или *?')
operation = input()
a=int(input('перше число: '))
b=int(input('друге число: '))
if operation == '+':
   print(a+b)
elif operation == '-':
   print(a-b)
elif operation == '/':
   print(a/b)
elif operation == '*':
   print(a*b)
else:
   print('Неизвестная операция')


