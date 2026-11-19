import flet as ft


#Main Function, Page Declaration and Naming
def main_menu (page: ft.Page):
    #add padding so objects dont stick to the absolute edges (30 pixels)
    page.padding = 30

    #Name the Page
    page.title = "Kyle's Bomb Game"
    
    #Put objects starting at the top going down (works with horizontal alignment)
    page.vertical_alignment = ft.MainAxisAlignment.START
    #center all objects in the middle (horizontal axis, this results in a vertical line due to working with the previous alignment)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    #create a container to put the text in, for location purposes
    page.add(
        ft.Container(
            content=ft.Text(
                value="Bomb Game", 
                color="Black",
                size=60,   
            ),
            bgcolor="Grey",
            padding=15,
            border_radius=12,
        )
    )


ft.run(main_menu)