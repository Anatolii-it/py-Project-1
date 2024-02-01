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
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("The Enchanted Nightingale"),
                            subtitle=ft.Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("o"),
                                ft.TextButton("x"),
                                ft.TextButton("x")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                        ft.Row(
                            [ft.TextButton("o", tooltip = "Exit",on_click = on_click), #позволяет обработать нажатие и вихід
                                ft.TextButton("x"),
                                ft.TextButton("x")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                        ft.Row(
                            [ft.TextButton("x"),
                                ft.TextButton("o"),
                                ft.TextButton("x")
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

ft.app(target=main)