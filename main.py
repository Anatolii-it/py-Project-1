
def my_sum(x, y):
    s = 0
    for number in range(x, y +1 ):
        s = s + number
    print("Сума між початковим та кінцевим", s)
x=int(input("Введіть початковє значення - "))
y=int(input("Введіть кінцеве значення - "))
s = c = 0
if __name__ == '__main__':
    result = my_sum(x,y)
    print(result)
my_sum(x,y)