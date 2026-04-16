import flet as ft

def main(page: ft.Page):
    page.title = "AGA GLOBAL | BASELINE"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def on_click(e):
        page.add(ft.Text("SYSTEM ONLINE: Handshake Successful", color="#00FF41"))
        page.update()

    page.add(
        ft.Column([
            ft.Text("AGA GLOBAL TECH", size=30, weight="bold", color="#00FF41"),
            ft.Text("LENS AI: ENGINE TEST", color="#555555"),
            ft.Divider(color="#222222"),
            ft.ElevatedButton("TEST HANDSHAKE", on_click=on_click),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
  
