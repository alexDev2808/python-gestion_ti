import flet as ft
from controllers.personal_controller import login


def login_view(page: ft.Page):

    txt_usuario = ft.TextField(
        label="ID Empleado",
        prefix_icon=ft.icons.PERSON,
        width=300,
        color=ft.colors.WHITE,
        border_color=ft.colors.BLUE_400,
        focused_border_color=ft.colors.BLUE_200,
        label_style=ft.TextStyle(color=ft.colors.BLUE_200),
    )

    txt_password = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=300,
        color=ft.colors.WHITE,
        border_color=ft.colors.BLUE_400,
        focused_border_color=ft.colors.BLUE_200,
        label_style=ft.TextStyle(color=ft.colors.BLUE_200),
    )

    txt_error = ft.Text(
        value="",
        color=ft.colors.RED_400,
        size=13,
    )

    btn_loading = ft.ProgressRing(
        width=20,
        height=20,
        stroke_width=2,
        color=ft.colors.WHITE,
        visible=False,
    )

    def handle_login(e):
        txt_error.value = ""

        if not txt_usuario.value.strip():
            txt_error.value = "Ingresa tu ID de empleado."
            page.update()
            return

        if not txt_password.value.strip():
            txt_error.value = "Ingresa tu contraseña."
            page.update()
            return

        btn_loading.visible = True
        btn_ingresar.disabled = True
        page.update()

        empleado = login(txt_usuario.value.strip(), txt_password.value.strip())

        btn_loading.visible = False
        btn_ingresar.disabled = False

        if empleado:
            page.session.set("empleado", empleado)
            page.go("/dashboard")
        else:
            txt_error.value = "ID o contraseña incorrectos."

        page.update()

    btn_ingresar = ft.ElevatedButton(
        text="Ingresar",
        width=300,
        height=45,
        bgcolor=ft.colors.BLUE_600,
        color=ft.colors.WHITE,
        on_click=handle_login,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
    )

    card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(name=ft.icons.PEOPLE_ALT_ROUNDED, size=70, color=ft.colors.BLUE_300),
                ft.Text("Gestión Personal", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.Text("Inicia sesión para continuar", size=13, color=ft.colors.BLUE_GREY_300),
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                txt_usuario,
                txt_password,
                txt_error,
                ft.Divider(height=5, color=ft.colors.TRANSPARENT),
                ft.Row(controls=[btn_ingresar, btn_loading], alignment=ft.MainAxisAlignment.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
        ),
        padding=40,
        bgcolor=ft.colors.BLUE_GREY_800,
        border_radius=16,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=20, color=ft.colors.BLACK45),
    )

    return ft.View(
        route="/",
        bgcolor=ft.colors.BLUE_GREY_900,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[card],
    )