
import flet as ft
import random


def main(page: ft.Page):
    page.title = "A greeting flet app by Ido"
    page.padding = 0
    page.spacing = 0

    first_name = ft.TextField(
        label="First Name",
        width=300
    )

    last_name = ft.TextField(
        label="Last Name",
        width=300
    )

    greeting = ft.Text(size=20)

    logos = []

    def create_logo():
        return ft.Container(
            content=ft.Image(
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2GhGRqfDTApmn_JO7HLeI0gKi7pQSqf4m_Q-1PXf3gRUfSZBHjqoTJT2q&s=10",
                width=35,
                height=35
            ),
            width=35,
            height=35,
            left=random.randint(10, 800),
            top=-60
        )

    for _ in range(50):
        logos.append(create_logo())

    logo_stack = ft.Stack(
        controls=logos,
        expand=True
    )

    def drop_logos(e):
        for logo in logos:
            logo.animate_position = None
            logo.left = random.randint(10, 800)
            logo.top = random.randint(-150, -30)

        page.update()

        for logo in logos:
            logo.animate_position = ft.Animation(
                duration=random.randint(800, 1400),
                curve=ft.AnimationCurve.EASE_IN
            )
            logo.top = random.randint(850, 1000)

        page.update()

    def greet(e):
        greeting.value = (
            f"Welcome, {first_name.value} {last_name.value}"
        )
        page.update()

    greeting_button = ft.GestureDetector(
        content=ft.Button(
            "Press for a greeting!",
            on_click=greet
        ),
        on_long_press=drop_logos
    )

    content_column = ft.Column(
        controls=[
            first_name,
            last_name,
            greeting_button,
            greeting
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
                controls=[content_column],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        ]
    )

    page.add(root_stack)


ft.run(main)
