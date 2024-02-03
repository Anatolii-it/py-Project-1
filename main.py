import flet as ft

x = y = step = 0
desk = [[" " for _ in range(3)] for _ in range(3)]
sim = ["X", "O"]

def main(page):
    page.title = "крестики нолики"

    def check_victory(desk, s):
        #print("перевірка на перемогу")
        for m_string in desk:
            if all(s == i for i in m_string):
                return True
        for st in range(3):
            if all(desk[m_string][st] == s for m_string in range(3)):
                return True
        if all(desk[i][i] == s for i in range(3)) or all(desk[i][2 - i] == s for i in range(3)):
            return True
        return False

    def steps(x, y):
        global step
        try:
            while (step >= 0):
                lin, st = (x, y)
                #st = y
                #print(desk)

                #w_desk(desk)
                if desk[lin][st] == " ":
                    desk[lin][st] = sim[step % 2]
                    if check_victory(desk, sim[step % 2]):
                        #w_desk(desk)
                        print(f"Гравець {sim[step % 2]} здобув перемогу!")
                        break
                    step += 1
                else:
                    print("ця клитина зайнята ." )
                return check_victory(desk,sim[step % 2])
        except Exception as e:
            print(e)

    def on_click(x, y):
        #page.window_close(),
        return steps(x, y)



    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text("Крестики нолики"),
                            subtitle=ft.Text(
                                "Rules: Click on an empty square to make a move. First move - X."
                            ),
                        ),
                        ft.Row(
                            [
                                ft.Container(

                                    content=ft.Text(sim[step % 2]),
                                    margin=10,
                                    padding=10,
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.colors.CYAN_200,
                                    width=50,
                                    height=50,
                                    border_radius=10,
                                    ink=True,
                                    on_click=lambda e: on_click(0,  0,),


                                ),
                                ft.Container(
                                    content=ft.Text("2"),
                                    margin=10,
                                    padding=10,
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.colors.CYAN_200,
                                    width=50,
                                    height=50,
                                    border_radius=10,
                                    ink=True,
                                    on_click=lambda e: on_click(0, 1, )
                                ),
                                ft.Container(
                                    content=ft.Text("3"),
                                    margin=10,
                                    padding=10,
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.colors.CYAN_200,
                                    width=50,
                                    height=50,
                                    border_radius=10,
                                    ink=True,
                                    on_click=lambda e: on_click(0, 2, )
                                ),
                                # Add similar containers for other cells
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                        ft.Row(
                            [
                                ft.Container(
                                content=ft.Text("1"),
                                margin=10,
                                padding=10,
                                alignment=ft.alignment.center,
                                bgcolor=ft.colors.CYAN_200,
                                width=50,
                                height=50,
                                border_radius=10,
                                ink=True,
                                on_click=lambda e: on_click(1, 0, )
                            ),
                                ft.Container(
                                    content=ft.Text("2"),
                                    margin=10,
                                    padding=10,
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.colors.CYAN_200,
                                    width=50,
                                    height=50,
                                    border_radius=10,
                                    ink=True,
                                    on_click=lambda e: on_click(1, 1, )
                                ),
                                ft.Container(
                                    content=ft.Text("3"),
                                    margin=10,
                                    padding=10,
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.colors.CYAN_200,
                                    width=50,
                                    height=50,
                                    border_radius=10,
                                    ink=True,
                                    on_click=lambda e: on_click(1, 2, )
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                        ft.Row(
                            [
                                ft.Container(
                                content=ft.Text("1"),
                                margin=10,
                                padding=10,
                                alignment=ft.alignment.center,
                                bgcolor=ft.colors.CYAN_200,
                                width=50,
                                height=50,
                                border_radius=10,
                                ink=True,
                                on_click=lambda e: on_click(2, 0, )
                            ),
                                ft.Container(
                                    content=ft.Text("2"),
                                    margin=10,
                                    padding=10,
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.colors.CYAN_200,
                                    width=50,
                                    height=50,
                                    border_radius=10,
                                    ink=True,
                                    on_click=lambda e: on_click(2, 1, )
                                ),
                                ft.Container(
                                    content=ft.Text("3"),
                                    margin=10,
                                    padding=10,
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.colors.CYAN_200,
                                    width=50,
                                    height=50,
                                    border_radius=10,
                                    ink=True,
                                    on_click=lambda e: on_click(2, 2, )
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        )
                    ]
                )
            )
        )
    )
ft.app(target=main)