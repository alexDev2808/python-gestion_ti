import flet as ft
from controllers.personal_controller import login
from theme import Colors, TextStyles, text_field, primary_button, card


def login_view(page: ft.Page) -> ft.Container:

    txt_usuario  = text_field("Num. Empleado", ft.Icons.ACCOUNT_CIRCLE)
    txt_password = text_field("Contraseña",  ft.Icons.LOCK, password=True)

    txt_error = ft.Text(value="", color=Colors.ERROR, size=13)

    btn_loading = ft.ProgressRing(
        width=20, height=20, stroke_width=2,
        color=Colors.TEXT_PRIMARY, visible=False,
    )

    def handle_login(e):
        txt_error.value = ""

        if not txt_usuario.value.strip():
            txt_error.value = "Escribe tu número de empleado."
            page.update()
            return

        if not txt_password.value.strip():
            txt_error.value = "Escribe tu contraseña."
            page.update()
            return

        btn_loading.visible = True
        btn_ingresar.disabled = True
        page.update()

        empleado = login(txt_usuario.value.strip(), txt_password.value.strip())

        btn_loading.visible = False
        btn_ingresar.disabled = False

        if empleado:
            page.data = {"empleado": empleado}
            # TODO: navegar al dashboard cuando exista
            page.clean()
            page.add(ft.Text(f"Bienvenido, {empleado.nombre_completo()}", color=Colors.TEXT_PRIMARY))
        else:
            txt_error.value = "Número de empleado o contraseña incorrectos."

        page.update()

    btn_ingresar = primary_button("Ingresar", on_click=handle_login)

    content = ft.Column(
        controls=[
            ft.Icon(ft.Icons.PEOPLE_ALT_ROUNDED, size=70, color=Colors.PRIMARY_LIGHT),
            ft.Text("Gestión TI", size=24, weight=ft.FontWeight.BOLD, color=Colors.TEXT_PRIMARY),
            ft.Text("Inicia sesión para continuar", size=13, color=Colors.TEXT_SECONDARY),
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            txt_usuario,
            txt_password,
            txt_error,
            ft.Divider(height=5, color=ft.Colors.TRANSPARENT),
            ft.Row(
                controls=[btn_ingresar, btn_loading],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=12,
    )

    return card(content)
