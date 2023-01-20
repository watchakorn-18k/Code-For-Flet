import flet as ft


def main(page):
    page.title = "ListTile Examples"
    page.auto_scroll = True
    for i in range(0, 5):
        page.add(ft.ListTile(
            title=ft.Text(f"บทที่ {i} การใช้งาน Python"),
            subtitle=ft.Text("คลิกเพื่อดูรายละเอียด"),
            leading=ft.Text(i),
            trailing=ft.Text("หนึ่ง"),
            autofocus=True,
            content_padding=ft.padding.only(
                top=50, left=50, right=50, bottom=20),
            dense=True,
            on_click=lambda x: print("1"),
            on_long_press=lambda x: print("5555")
        ))


ft.app(target=main)
