import flet as ft
from controllers.personal_controller import login

def main(page: ft.Page):
    page.title = "Gestión Personal - Login"
    page.window_width = 450
    page.window_height = 650
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- Elementos de la interfaz con iconos corregidos ---
    txt_usuario = ft.TextField(
        label="ID Empleado",
        prefix_icon=ft.Icon(ft.Icons.ACCOUNT_CIRCLE), # Cambiado de PERSON a ACCOUNT_CIRCLE
        width=300,
    )

    txt_password = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icon(ft.Icons.PASSWORD), # Cambiado de LOCK a PASSWORD
        password=True,
        can_reveal_password=True,
        width=300,
    )

    txt_error = ft.Text(value="", color=ft.Colors.RED_400)

    def handle_login(e):
        if not txt_usuario.value or not txt_password.value:
            txt_error.value = "Completa todos los campos"
            page.update()
            return
        
        try:
            # Intentar conectar con la BD
            empleado = login(txt_usuario.value, txt_password.value)
            
            if empleado:
                page.clean()
                page.add(ft.Text(f"Bienvenido {empleado.nombre_completo()}"))
            else:
                txt_error.value = "Credenciales incorrectas"
        except Exception as ex:
            txt_error.value = f"Error de BD: {ex}"
        
        page.update()

    btn_ingresar = ft.ElevatedButton(
        content="Ingresar",
        width=300,
        on_click=handle_login,
        style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)
    )

    # --- Contenedor Principal con icono corregido ---
    login_card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(ft.Icons.SUPERVISOR_ACCOUNT, size=50, color=ft.Colors.BLUE_400),
                ft.Text("Inicio de Sesión", size=25, weight=ft.FontWeight.BOLD),
                ft.Divider(height=20),
                txt_usuario,
                txt_password,
                txt_error,
                btn_ingresar
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        padding=40,
        bgcolor=ft.Colors.GREY_900,
        border_radius=20,
        border=ft.border.all(1, ft.Colors.GREY_800)
    )

    page.add(login_card)

if __name__ == "__main__":
    ft.app(target=main)