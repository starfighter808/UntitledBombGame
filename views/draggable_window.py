import flet as ft

class DraggableWindow(ft.Container):
    def __init__(self, title: str, content: ft.Control, left: float = 50, top: float = 50, width: float = 320, on_focus=None):
        super().__init__()
        self.left = left
        self.top = top
        self.width = width
        self.on_focus = on_focus
        self.bgcolor = ft.Colors.BLUE_GREY_800
        self.border = ft.Border.all(2, ft.Colors.BLUE_GREY_400)
        self.border_radius = 8
        self.shadow = ft.BoxShadow(blur_radius=12, color=ft.Colors.BLACK_54)

        # Title bar acts as the drag handle
        title_bar = ft.GestureDetector(
            on_pan_start=self._on_drag_start,
            on_pan_update=self._on_drag,
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.DRAG_INDICATOR, size=16, color=ft.Colors.WHITE_70),
                        ft.Text(title, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, size=14),
                    ],
                ),
                bgcolor=ft.Colors.BLUE_GREY_900,
                padding=ft.Padding.symmetric(horizontal=10, vertical=8),
                border_radius=ft.BorderRadius.only(top_left=6, top_right=6),
            ),
        )

        self.content = ft.Column(
            [
                title_bar,
                ft.Container(content=content, padding=12),
            ],
            spacing=0,
        )

    def _on_drag_start(self, e: ft.DragStartEvent):
        if self.on_focus:
            self.on_focus(self)

    def _on_drag(self, e: ft.DragUpdateEvent):
        self.left = max(0, self.left + e.local_delta.x)
        self.top = max(0, self.top + e.local_delta.y)
        self.update()
