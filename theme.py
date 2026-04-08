import flet as ft


class Colors:
    PRIMARY        = ft.Colors.BLUE_600
    PRIMARY_LIGHT  = ft.Colors.BLUE_300
    SURFACE        = ft.Colors.BLUE_GREY_800
    BACKGROUND     = ft.Colors.BLUE_GREY_900
    BORDER         = ft.Colors.BLUE_400
    BORDER_FOCUS   = ft.Colors.BLUE_200
    TEXT_PRIMARY   = ft.Colors.WHITE
    TEXT_SECONDARY = ft.Colors.BLUE_GREY_300
    TEXT_LABEL     = ft.Colors.BLUE_200
    ERROR          = ft.Colors.RED_400
    SHADOW         = ft.Colors.BLACK45


class TextStyles:
    TITLE    = ft.TextStyle(size=24, weight=ft.FontWeight.BOLD, color=Colors.TEXT_PRIMARY)
    SUBTITLE = ft.TextStyle(size=13, color=Colors.TEXT_SECONDARY)
    LABEL    = ft.TextStyle(color=Colors.TEXT_LABEL)
    ERROR    = ft.TextStyle(size=13, color=Colors.ERROR)


def text_field(label: str, icon, password: bool = False) -> ft.TextField:
    return ft.TextField(
        label=label,
        prefix_icon=icon,
        password=password,
        can_reveal_password=password,
        width=300,
        color=Colors.TEXT_PRIMARY,
        border_color=Colors.BORDER,
        focused_border_color=Colors.BORDER_FOCUS,
        label_style=TextStyles.LABEL,
    )


def primary_button(text: str, on_click, width: int = 300) -> ft.ElevatedButton:
    return ft.ElevatedButton(
        content=text,
        width=width,
        height=45,
        bgcolor=Colors.PRIMARY,
        color=Colors.TEXT_PRIMARY,
        on_click=on_click,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )


def card(content: ft.Control) -> ft.Container:
    return ft.Container(
        content=content,
        padding=40,
        bgcolor=Colors.SURFACE,
        border_radius=16,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=20, color=Colors.SHADOW),
    )


FONT_FAMILY = "Rubik"

APP_THEME = ft.Theme(
    color_scheme_seed=ft.Colors.BLUE,
    font_family=FONT_FAMILY,    
)
