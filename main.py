import flet as ft

def main(page):
    page.title = "Card Example"

    def on_click(e):
        page.window_close(),
    appbar = ft.AppBar(
        center_title=True,
        title=ft.Text("Крестікі нолікі"),
        leading=ft.Icon(name=ft.icons.TERMINAL),
        actions=[
            ft.IconButton(
                icon=ft.icons.SETTINGS,
                tooltip="Settings",
            ),
            ft.IconButton(
                icon=ft.icons.EXIT_TO_APP_ROUNDED,
                tooltip="Exit",
                on_click=on_click,
            ),
        ],
    )
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
                            on_click=lambda e: (x := 1, y := 1, print("Clickable with Ink clicked!", x, y)),
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
                            on_click=lambda e: (x := 2, y := 1, print("Clickable with Ink clicked!", x, y)),
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
                            on_click=lambda e: (x := 3 , y := 1 , print("Clickable with Ink clicked!",x,y)),
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
                                on_click=lambda e: (x := 1, y := 2, print("Clickable with Ink clicked!", x, y)),
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
                                    on_click=lambda e: (x := 2, y := 2, print("Clickable with Ink clicked!", x, y)),
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
                                    on_click=lambda e: (x := 3, y := 2, print("Clickable with Ink clicked!", x, y)),
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
                                on_click=lambda e: (x := 1 , y := 3, print("Clickable with Ink clicked!", x, y)),
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
                                    on_click=lambda e: (x := 2 , y := 3, print("Clickable with Ink clicked!", x, y)),
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
                                    on_click=lambda e: (x := 3 , y := 3, print("Clickable with Ink clicked!", x, y)),
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
x=y=0
ft.app(target=main)