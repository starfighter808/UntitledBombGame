

print("importing flet")
import flet as ft

print("importing main menu")
from views.main_menu import MainMenuView
print("importing game view")
from views.game import GameView
#Main Function, Page Declaration and Naming
def main (page: ft.Page):
    print("main triggered via flet")
    #Name the Page
    page.title = "Kyle's Bomb Game"
    
    #this route variable is used to separate the screens (game/settings?/menu)
    def route_change(route):
        print("Route Change triggered with route {page.route}")
        page.views.clear()

        #check the current route and show the correct view
        if page.route == "/":
            print("loading main menu")
            page.views.append(MainMenuView(page))
            print("main menu loaded, appended to views")
        elif page.route == "/game":
            print("loading game view")
            page.views.append(GameView(page))
            print("game loaded, appended to views")


        #this line pushes all changes to the current screen and displays them for the user
        page.update()
        print("page updated")
    
    def view_pop(view):
        print("view_pop triggered")
        #remove the top view from the stack
        page.views.pop()

        #set top_view equal to whichever screen is now the top screen
        top_view = page.views[-1]

        #navigate to that screen's route
        page.navigate(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    print("triggering initial page load")
    page.route = "/"
    page.views.append(MainMenuView(page))
    page.update()

print("calling main")
ft.run(main)