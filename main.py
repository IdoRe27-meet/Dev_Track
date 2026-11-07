import flet as ft
import asyncio
import random
import string

async def main(page: ft.Page):
    page.title = "A greeting flet app by Ido"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    first_name = ft.TextField(label="First Name")
    last_name = ft.TextField(label="Last Name")
    greeting = ft.Text(size=20, weight=ft.FontWeight.BOLD)

    async def rain_worker(e=None):
        logo_url = "https://cdn.prod.website-files.com/5dd64bd3a930f9d04abd1363/5de254f85f1762feee30d664_meet_logo_red.png"
        
        try:
            w = int(page.window.width) if page.window.width else int(page.window_width)
            h = int(page.window.height) if page.window.height else int(page.window_height)
        except:
            w, h = 2500, 1500

        falling_logos = []
        for _ in range(60):
            logo = ft.Container(
                content=ft.Image(src=logo_url, width=60),
                left=random.randint(0, max(w, 500)),
                top=-100,
                animate_position=ft.Animation(random.randint(2000, 3500), ft.AnimationCurve.EASE_IN)
            )
            falling_logos.append(logo)

        page.overlay.extend(falling_logos)
        page.update()
        await asyncio.sleep(0.05)

        for logo in falling_logos:
            logo.top = h + 200
        page.update()

        await asyncio.sleep(4.0)
        for logo in falling_logos:
            if logo in page.overlay:
                page.overlay.remove(logo)
        page.update()

    async def greet(e):
        val1_raw = first_name.value or ""
        val2_raw = last_name.value or ""
        val1 = val1_raw.lower().strip()
        val2 = val2_raw.lower().strip()

        if val1_raw.strip().isnumeric() and val2_raw.strip().isnumeric():
            total = int(val1_raw.strip()) + int(val2_raw.strip())
            greeting.value = f"Calculator Mode: {val1_raw.strip()} + {val2_raw.strip()} = {total}"
        
        elif val1 == "change" and val2 == "color":
            greeting.value = "The color has changed!"
            colors = [ft.Colors.RED, ft.Colors.BLUE, ft.Colors.GREEN, ft.Colors.YELLOW, ft.Colors.PURPLE, ft.Colors.CYAN]
            page.bgcolor = random.choice(colors)
        
        elif val1 == "gen" and val2 == "pass":
            chars = string.ascii_letters + string.digits + "!@#$%^&*"
            password = ''.join(random.choice(chars) for _ in range(12))
            greeting.value = f"New Password: {password}"
        
        elif val1 == "boom":
            for i in range(5, 0, -1):
                greeting.value = f"Closing app in {i}..."
                greeting.color = ft.Colors.RED
                page.update()
                await asyncio.sleep(1)
            await page.window.destroy()
            return
        
        elif val1 == "reverse":
            reversed_text = val2_raw[::-1]
            greeting.value = f"Welcome, {reversed_text}!"
        
        elif val1 == "rename" and val2_raw:
            btn.content.value = val2_raw
            greeting.value = "Button renamed!"
        
        elif val1 == "31" and val2 =="05":
            page.bgcolor = ft.Colors.BLUE_900
            greeting.value = "Happy BD!"


        else:
            page.bgcolor = None
            greeting.color = None
            greeting.value = f"Welcome, {val1_raw} {val2_raw}!".strip()
        
        page.update()

    btn = ft.Button(
        content=ft.Text("Press for a greeting!"), 
        on_click=greet, 
        on_long_press=rain_worker
    )

    page.add(first_name, last_name, btn, greeting)

ft.run(main)