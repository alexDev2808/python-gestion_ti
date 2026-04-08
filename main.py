import flet as ft
from config import APP_TITLE
from theme import Colors, APP_THEME
from views.login_view import login_view


def main(page: ft.Page):
    page.fonts = {
        "Rubik": "https://fonts.gstatic.com/s/rubik/v28/iJWZBXyIfDnIV5PNhY1KTN7Z-Yh-B4iFU0U1Z4Y.woff2"
    }
    page.title = APP_TITLE
    page.theme = APP_THEME
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = Colors.BACKGROUND
    page.window_width = 450
    page.window_height = 650
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(login_view(page))


if __name__ == "__main__":
    ft.app(target=main)
