from time import sleep
import flet as ft
import datetime


def main(page: ft.Page):
    page.title = "Auto-scrolling ListView"

    lv = ft.ListView(expand=1, spacing=10, padding=20,
                     auto_scroll=True)

    count = 1

    for i in range(0, 60):
        lv.controls.append(ft.Text(datetime.datetime.now()))
        count += 1

    page.add(lv)

    for i in range(0, 60):
        sleep(1)
        lv.controls.append(ft.Text(datetime.datetime.now()))
        count += 1
        page.update()


ft.app(target=main)
