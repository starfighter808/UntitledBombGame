import flet as ft

def create_menu_view(on_start_click):
    #create Text object
    title_text = ft.Text(
        value="Bomb Game",
        color="Black",
        size=60,
    )

    #put text object in white container
    title_container = ft.Container(
        content=title_text,
        bgcolor="White",
        padding=15,
        border_radius=12,
    )

    start_button = ft.Button(
        content="Begin Countdown...",
        on_click=on_start_click
    )

    return ft.Column(
        [
            title_container, 
            start_button
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
    )
