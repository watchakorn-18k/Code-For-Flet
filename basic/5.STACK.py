import flet
from flet import CircleAvatar, Container, Stack, alignment, colors, ElevatedButton


def main(page):

    status = CircleAvatar(bgcolor=colors.GREEN, radius=5)

    def change_status():
        status.bgcolor = colors.RED if status.bgcolor == colors.GREEN else colors.GREEN
        page.update()
        
    page.add(
        Stack(
            [
                CircleAvatar(
                    foreground_image_url="https://static.vecteezy.com/system/resources/thumbnails/003/350/177/small/avatar-man-person-design-free-vector.jpg"
                ),
                Container(
                    content=status,
                    alignment=alignment.bottom_left,
                ),
            ],
            width=40,
            height=40,
        )
    )
    page.add(Container(
        content=ElevatedButton(text="เปลี่ยนสถานะ",on_click=lambda e: change_status()),
        alignment=alignment.center
    ))


flet.app(target=main, view=flet.WEB_BROWSER)
