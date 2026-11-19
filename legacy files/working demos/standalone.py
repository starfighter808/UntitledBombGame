import flet as ft
def main(page: ft.Page):
    page.title = "Kyle's Bomb Game"
    page.bgcolor = ft.Colors.BLUE_GREY_900
    
    title_text = ft.Text(value="Bomb Game", color=ft.Colors.WHITE, size=50)
    title_container = ft.Container(
        content=title_text,
        bgcolor=ft.Colors.RED_700,
        padding=20,
        border_radius=12,
    )
    
    def start_game(e):
        print("Switching to game view...")
        page.clean()
        page.add(
            ft.Text("Game Screen Active!", size=30, color=ft.Colors.WHITE),
            ft.Button(content="Back to Menu", on_click=go_to_menu)
        )
        page.update()

    def go_to_menu(e):
        print("Returning to menu...")
        page.clean()
        page.add(title_container, start_button)
        page.update()

    start_button = ft.Button(
        content="Begin Countdown...",
        on_click=start_game
    )

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(title_container, start_button)

ft.run(main)