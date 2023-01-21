import flet as ft


def main(page: ft.Page):
    page.title = "GridView"
    page.theme_mode = ft.ThemeMode.DARK
    page.update()
    grid = ft.GridView(
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=50,
        runs_count=5,
        run_spacing=15,
        padding=50,
    )

    for i in range(0, 10):
        grid.controls.append(ft.Text(i))

    page.add(grid)


ft.app(target=main)
