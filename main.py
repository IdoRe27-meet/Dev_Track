# Sick Code Along
import flet as ft

def main(page: ft.Page):
    page.title = "A greeting flet app by Ido"
    first_name = ft.TextField(label="First Name")
    last_name = ft.TextField(label="Last Name")
    greeting = ft.Text()

    def greet(e):
        greeting.value = f"Welcome, {first_name.value} {last_name.value}"
        page.update()

    page.add(first_name,last_name,ft.Button("Prees for a greeting!", on_click = greet), greeting)

ft.run(main)


