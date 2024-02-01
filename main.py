def w_desk(desk):
    for m_string in desk:
        print(" | ".join(m_string))
        print("-" * 9)

def check_viktory(desk, s):
    for m_string in desk:
        if all(s == i for i in m_string):
            return True
    for st in range(3):
        if all(desk[m_string][st] == s for m_string in range(3)):
            return True
    if all(desk[i][i] == s for i in range(3)) or all(desk[i][2 - i] == s for i in range(3)):
        return True
    return False

desk = [[" " for _ in range(3)] for _ in range(3)]
step = 0
sim = ["X", "O"]

while True:
    w_desk(desk)
    lin, st = map(int, input(f"Гравець {step % 2 + 1}, зробіть хід через пробіл наприклад 0 0: ").split())
    if desk[lin][st] == " ":
        desk[lin][st] = sim[step % 2]
        if check_viktory(desk, sim[step % 2]):
            w_desk(desk)
            print(f"Гравець {step % 2 + 1} Виграв!")
            break
        step += 1
    else:
        print("Ця клитинка зайнята спробуйте іншу.")