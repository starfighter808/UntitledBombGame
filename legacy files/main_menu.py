import flet as ft

def MainMenuView(page: ft.Page):
    return ft.View(
        "/",
        [
            #REQUIRED FOR BACKGROUD FLET STRUCTURE
            ft.AppBar(title=ft.Text("Kyle's Bomb Game")),

            ft.Container(
                        content=ft.Text(
                                value="Bomb Game", 
                                color="Black",
                                size=60,   
                        ),
                        bgcolor="White",
                        padding=15,
                        border_radius=12,
            ),
            ft.Button(
                content="Begin Countdown...",
                on_click=lambda e: page.go("/game")
            ),
        ],
        bgcolor="Black",
        #Put objects starting at the top going down (works with horizontal alignment)
        vertical_alignment = ft.MainAxisAlignment.START,
        #center all objects in the middle (horizontal axis, this results in a vertical line due to working with the previous alignment)
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
    )