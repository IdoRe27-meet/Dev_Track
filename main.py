import flet as ft
import random

def main(page: ft.Page):
    page.title = "A greeting flet app by Ido"
    page.padding = 0

    first_name = ft.TextField(label="First Name", width=300)
    last_name = ft.TextField(label="Last Name", width=300)
    greeting = ft.Text(size=20)

    logos = []
    for i in range(50):
        logos.append(
            ft.Image(
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2GhGRqfDTApmn_JO7HLeI0gKi7pQSqf4m_Q-1PXf3gRUfSZBHjqoTJT2q&s=10",
                width=35,
                height=35,
                left=random.randint(10, 800),
                top=-60,
                animate_position=ft.Animation(
                    duration=1000,
                    curve=ft.AnimationCurve.EASE_IN
                )
            )
        )

    logo_stack = ft.Stack(
        expand=True,
        controls=logos
    )

    def drop_logos(e):
        for logo in logos:
            logo.animate_position = None
            logo.top = random.randint(-150, -30)
            logo.left = random.randint(10, 800)
            logo.update()
        
        page.update()

        for logo in logos:
            logo.animate_position = ft.Animation(
                duration=random.randint(800, 1400),
                curve=ft.AnimationCurve.EASE_IN
            )
            logo.top = random.randint(850, 1000)
            logo.update()

    def greet(e):
        greeting.value = f"Welcome, {first_name.value} {last_name.value}"
        greeting.update()

    content_column = ft.Column(
        [
            first_name,
            last_name,
            ft.Button("Prees for a greeting!", on_click=greet, on_long_press=drop_logos),
            greeting,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        tight=True
    )

    root_stack = ft.Stack(
        expand=True,
        controls=[
            logo_stack,
            ft.Row(
                [content_column],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        ]
    )

    page.add(root_stack)

ft.run(main)