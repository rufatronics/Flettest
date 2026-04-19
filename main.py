import flet as ft
import flet_camera as fc

def main(page: ft.Page):
    # --- Tactical UI Config ---
    page.title = "AGA GLOBAL | LENS AI"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    page.padding = 15
    page.window_resizable = False

    status_text = ft.Text("SENSOR: INITIALIZING...", color="#555555", font_family="monospace")

    # --- Native Camera Control ---
    # This uses the phone's built-in drivers (No OpenCV needed)
    cam = fc.Camera(
        expand=True,
        on_init=lambda _: setattr(status_text, "value", "SENSOR: ONLINE | 30FPS"),
        on_error=lambda e: setattr(status_text, "value", f"SYSTEM ERROR: {e.data}"),
    )

    # --- The HUD Layout ---
    page.add(
        ft.Column([
            # Branding Header
            ft.Row([
                ft.Text("AGA GLOBAL TECH", size=22, weight="bold", color="#00FF41"),
                ft.Icon(ft.icons.SHIELD_ROUNDED, color="#00FF41", size=20)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            
            status_text,
            
            # The "Eyes" of the App
            ft.Container(
                content=cam,
                border_radius=20,
                border=ft.border.all(2, "#222222"),
                bgcolor="#000000",
                expand=True,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS
            ),
            
            # Tactical Controls
            ft.Row([
                ft.FloatingActionButton(
                    icon=ft.icons.FLIP_CAMERA_ANDROID,
                    bgcolor="#00FF41",
                    on_click=lambda _: cam.flip_camera(),
                    tooltip="Switch Camera"
                ),
                ft.FloatingActionButton(
                    icon=ft.icons.CAMERA_ALT,
                    bgcolor="#111111",
                    on_click=lambda _: cam.take_picture(),
                    tooltip="Capture Frame"
                ),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            
            ft.Text("V2.5 | NATIVE KERNEL", size=10, color="#333333")
        ], expand=True)
    )
    page.update()

ft.app(target=main)
    
