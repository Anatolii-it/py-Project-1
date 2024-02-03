import flet as ft

x = y = step = 0
desk = [[" " for _ in range(3)] for _ in range(3)]
sim = ["X", "O"]

def main(page):
    page.title = "Крестики-нолики"

    def check_victory(desk, s):
        for m_string in desk:
            if all(s == i for i in m_string):
                return True
        for st in range(3):
            if all(desk[m_string][st] == s for m_string in range(3)):
                return True
        if all(desk[i][i] == s for i in range(3)) or all(desk[i][2 - i] == s for i in range(3)):
            return True
        return False

    def steps(x, y, step):
        try:
            lin, st = (x, y)

            if desk[lin][st] == " ":
                desk[lin][st] = sim[step % 2]
                if check_victory(desk, sim[step % 2]):
                    print(f"Гравець {sim[step % 2]} здобув перемогу!")
                return step + 1
            else:
                print("Ця клітина вже зайнята.")
            return step
        except Exception as e:
            print(e)

    def on_click(x, y, container):
        global step
        step = steps(x, y, step)
        container.content = ft.Text(sim[step % 2])

    text_widget = ft.Text(sim[step % 2])

    page.add(
        ft.Card(
            width = 480,
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text("Крестики-нолики"),
                            subtitle=ft.Text(
                                "Робіть ходи по черзі перший хід це- Х ."
                            ),
                        ),
                        ft.Row(
                            [
                                ft.Container(
                                    content=text_widget,
                                    margin=10,
                                    padding=10,
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.colors.CYAN_200,
                                    width=50,
                                    height=50,
                                    border_radius=10,
                                    ink=True,
                                    on_click=lambda e: on_click(0, 0, text_widget),
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
                                    on_click=lambda e: on_click(0, 1, text_widget),
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
                                    on_click=lambda e: on_click(0, 2, text_widget),
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
                                    on_click=lambda e: on_click(1, 0, text_widget),
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
                                    on_click=lambda e: on_click(1, 1, text_widget),
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
                                    on_click=lambda e: on_click(1, 2, text_widget),
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
                                    on_click=lambda e: on_click(2, 0, text_widget),
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
                                    on_click=lambda e: on_click(2, 1, text_widget),
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
                                    on_click=lambda e: on_click(2, 2, text_widget),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        )
                    ]
                )
            )
        )
    )
ft.app(target=lambda page: main(page))

#main(ft.Page(conn=None, session_id=None))
