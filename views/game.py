import flet as ft
from game_logic import BombLogic
from views.draggable_window import DraggableWindow

def create_game_view(page: ft.Page, on_back_click):
    # Expand the window into a desktop workspace
    page.window.width = 1200
    page.window.height = 800

    # --- 1. Build the Timer & Strike HUD Controls ---
    timer_text = ft.Text(
        value="05:00",
        size=48,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.RED_ACCENT_400,
        font_family="monospace",
    )

    strike_boxes = [
        ft.Container(
            content=ft.Text("X", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_800),
            width=36,
            height=36,
            alignment=ft.Alignment.CENTER,
            border=ft.Border.all(2, ft.Colors.GREY_700),
            border_radius=6,
            bgcolor=ft.Colors.BLACK_45,
        )
        for _ in range(3)
    ]

    status_text = ft.Text(value="STATUS: ARMED", size=13, color=ft.Colors.AMBER_400)

    hud_content = ft.Column(
        [
            ft.Row(strike_boxes, alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Container(
                content=timer_text,
                bgcolor=ft.Colors.BLACK,
                padding=ft.Padding.symmetric(horizontal=18, vertical=4),
                border_radius=8,
                border=ft.Border.all(2, ft.Colors.RED_900),
            ),
            status_text,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    # --- 2. Define BombLogic UI Callbacks ---
    def handle_time_update(time_str: str):
        timer_text.value = time_str
        if timer_text.page:
            timer_text.update()

    def handle_strike(current_strikes: int, max_strikes: int):
        for i in range(len(strike_boxes)):
            if i < current_strikes:
                strike_boxes[i].content.color = ft.Colors.RED_ACCENT_400
                strike_boxes[i].border = ft.Border.all(2, ft.Colors.RED_ACCENT_400)
                strike_boxes[i].bgcolor = ft.Colors.RED_900
        page.update()

    def handle_game_over(reason: str):
        status_text.value = reason
        status_text.color = ft.Colors.RED_ACCENT_400
        timer_text.color = ft.Colors.GREY_500
        page.update()

    # --- 3. Initialize & Start the Bomb ---
    bomb = BombLogic(
        on_time_update=handle_time_update,
        on_strike=handle_strike,
        on_game_over=handle_game_over,
        level_config={},
        duration=300,
        max_strikes=3,
    )
    page.run_task(bomb.run_timer)

    # --- 4. Set Up the Desktop Stack & Windows ---
    desktop_stack = ft.Stack(expand=True)

    def bring_to_front(window: DraggableWindow):
        # Move the clicked window to the end of the Stack list so it renders on top
        if window in desktop_stack.controls:
            desktop_stack.controls.remove(window)
            desktop_stack.controls.append(window)
            desktop_stack.update()

    hud_window = DraggableWindow(
        title="BOMB TIMER & STRIKES",
        content=hud_content,
        left=40,
        top=60,
        width=300,
        on_focus=bring_to_front,
    )

    # Temporary placeholder window to test overlapping & dragging
    test_module_window = DraggableWindow(
        title="MODULE: BUTTONDLE (TEST)",
        content=ft.Column(
            [
                ft.Text("Module UI will go here.", color=ft.Colors.WHITE),
                ft.Button(
                    content="Trigger Test Strike",
                    bgcolor=ft.Colors.RED_800,
                    color=ft.Colors.WHITE,
                    on_click=lambda e: bomb.issue_strike("Debug button"),
                ),
            ]
        ),
        left=380,
        top=60,
        width=320,
        on_focus=bring_to_front,
    )

    desktop_stack.controls.extend([hud_window, test_module_window])

    # --- 5. Top Control Bar (Cleanly stops timer on exit) ---
    def exit_to_menu(e):
        bomb.is_running = False
        on_back_click(e)

    top_bar = ft.Container(
        content=ft.Row(
            [
                ft.Button(content="← Abort & Return to Menu", on_click=exit_to_menu),
                ft.Text("Tip: Drag window title bars to rearrange modules", color=ft.Colors.WHITE_70, size=13),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=10,
        bgcolor=ft.Colors.BLACK_26,
    )

    return ft.Column(
        [
            top_bar,
            desktop_stack,
        ],
        expand=True,
        spacing=0,
    )
