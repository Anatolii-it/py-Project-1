def hyppi(s):
    a = [int(i) for i in s]
    if sum(a[:3]) == sum(a[3:]):
        print("True")
        return True
    else:
        print("False")
        return False

s = input("Введіть число для перевірки чи є щасливе - ")

hyppi(s)


