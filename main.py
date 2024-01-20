
def my_sum(x, y):
    s = 0
    for number in range(x, y +1 ):
        s = s + number
    print(s,end=' ')
x=int(input("Введіть початковє значення - "))
y=int(input("Введіть кінцеве значення - "))
s = c = 0
my_sum(x,y)