import flet as ft
def main(page: ft.Page):
    page.title = "Крестікі нолікі"
    page.padding = 0
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
    card = ft.Card(
        width=page.width * 0.8,
        height=page.height * 0.8,
        content=ft.Text("Hello World")

    )
    main_container = ft.Container(
        alignment=ft.alignment.center,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[
                "0xff00B2FF",
                "0xffA258FF",
                "0xffDB00FF",
            ],
            tile_mode=ft.GradientTileMode.MIRROR,
        ),
        expand=True,
    )
    column = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            card,
        ]
    )
    row = ft.Row(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            column,
        ]
    )
    padding = ft.Padding(top=10, bottom=0, left=0, right=0)
    stack = ft.Stack(
        expand=True,
        controls=[
            main_container,
            row,
        ]
    )
    page.appbar = appbar
    page.add(stack)
    page.update()
ft.app(target=main)