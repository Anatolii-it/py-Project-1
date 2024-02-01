def w_desk(desk):
    for m_string in desk:
        print(" | ".join(m_string))
        print("-" * 9)

def check_viktory(desk, s):
    # проверка строк
    for m_string in desk:
        if all(s == ячейка for ячейка in m_string):
            return True
    # проверка столбцов
    for столбец in range(3):
        if all(desk[m_string][столбец] == s for m_string in range(3)):
            return True
    # проверка диагоналей
    if all(desk[i][i] == s for i in range(3)) or all(desk[i][2 - i] == s for i in range(3)):
        return True
    return False

desk = [[" " for _ in range(3)] for _ in range(3)]
ход = 0
символы = ["X", "O"]

while True:
    w_desk(desk)
    ряд, столбец = map(int, input(f"Игрок {ход % 2 + 1}, введите строку и столбец (через пробел): ").split())
    if desk[ряд][столбец] == " ":
        desk[ряд][столбец] = символы[ход % 2]
        if check_viktory(desk, символы[ход % 2]):
            w_desk(desk)
            print(f"Игрок {ход % 2 + 1} выиграл!")
            break
        ход += 1
    else:
        print("Эта клетка уже занята. Попробуйте еще раз.")