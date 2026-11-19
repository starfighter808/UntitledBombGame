import flet as ft
from views.main_menu import create_menu_view
from views.game import create_game_view

def main(page: ft.Page):
    page.title = "Kyle's Bomb Game"
    #background color of the page
    page.bgcolor = ft.Colors.BLUE_GREY_900
    
    #Put objects starting at the top going down (works with horizontal alignment)
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    #center all objects in the middle (horizontal axis, this results in a vertical line due to working with the previous alignment)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def switch_to_game(e):
        page.clean()
        page.add(create_game_view(page, switch_to_menu))
        page.update()

    def switch_to_menu(e):
        page.clean()
        page.add(create_menu_view(switch_to_game))
        page.update()

    page.add(create_menu_view(switch_to_game))

ft.run(main)