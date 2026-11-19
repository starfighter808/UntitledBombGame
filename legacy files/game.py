import flet as ft

def GameView(page: ft.Page):
    return ft.View(
        "/game",
        [
            ft.Container(
                        content=ft.Text(
                                value="Bomb Game", 
                                color="Yellow",
                                size=60,   
                        ),
                        bgcolor="Grey",
                        padding=15,
                        border_radius=12,
            ),
        ],
        #Put objects starting at the top going down (works with horizontal alignment)
        vertical_alignment = ft.MainAxisAlignment.START,
        #center all objects in the middle (horizontal axis, this results in a vertical line due to working with the previous alignment)
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
    )