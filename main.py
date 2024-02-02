import flet as ft
x = y = (0)
def main(page):
    page.title = "Card Example"

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
    def on_click(e):
        page.window_close(),



    page.add(
        ft.Card(
            content=ft.Container(

                content=ft.Column(
                    [
                        ft.IconButton(
                            icon=ft.icons.EXIT_TO_APP_ROUNDED,
                            tooltip="Exit",
                            on_click=on_click,
                        ),
                        ft.ListTile(

                            title=ft.Text("давай зіграємо в крестікі нолікі"),
                            subtitle=ft.Text(
                                "Правила гри по черзі натисніть на пустий квадрат перший хід - х "
                            ),
                        ),
                        ft.Row(
                            [ft.Container(
                            content=ft.Text("1"),
                            margin=10,
                            padding=10,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.CYAN_200,
                            width=50,
                            height=50,
                            border_radius=10,
                            ink=True,
                            on_click=lambda e: (x := 0, y := 0, print("Clickable with Ink clicked!", x, y)),
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
                            on_click=lambda e: (x := 1, y := 0, print("Clickable with Ink clicked!", x, y)),
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
                            on_click=lambda e: (x := 2 , y := 0 , print("Clickable with Ink clicked!",x,y)),
                        ),
                    ],
                        alignment=ft.MainAxisAlignment.END,
                        ),
                        ft.Row(
                            [ft.Container(
                                content=ft.Text("1"),
                                margin=10,
                                padding=10,
                                alignment=ft.alignment.center,
                                bgcolor=ft.colors.CYAN_200,
                                width=50,
                                height=50,
                                border_radius=10,
                                ink=True,
                                on_click=lambda e: (x := 0, y := 1, print("Clickable with Ink clicked!", x, y)),
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
                                    on_click=lambda e: (x := 1, y := 1, print("Clickable with Ink clicked!", x, y)),
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
                                    on_click=lambda e: (x := 2, y := 1, print("Clickable with Ink clicked!", x, y)),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                        ft.Row(
                            [ft.Container(
                                content=ft.Text("1"),
                                margin=10,
                                padding=10,
                                alignment=ft.alignment.center,
                                bgcolor=ft.colors.CYAN_200,
                                width=50,
                                height=50,
                                border_radius=10,
                                ink=True,
                                on_click=lambda e: (x := 0 , y := 2, print("Clickable with Ink clicked!", x, y)),
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
                                    on_click=lambda e: (x := 1 , y := 2, print("Clickable with Ink clicked!", x, y)),
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
                                    on_click=lambda e: (lin := 2 , st := 2, print("Clickable with Ink clicked!", x, y)),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),

                    ]
                ),
                width=400,
                padding=10,
            )

        )
    )
    desk = [[" " for _ in range(3)] for _ in range(3)]
    step = 0
    sim = ["X", "O"]
    try:
        while True:
            w_desk(desk)
            lin  = x
            st = y
            print(lin,st),
            if desk[lin][st] == " ":
                desk[lin][st] = sim[step % 2]
                if check_viktory(desk, sim[step % 2]):
                    w_desk(desk)
                    print(f"Гравець {step % 2 + 1} Виграв!")
                    break
                step += 1
            else:
                print("Ця клитинка зайнята спробуйте іншу.")

    except Exception as e:
        print(e)

ft.app(target=main)