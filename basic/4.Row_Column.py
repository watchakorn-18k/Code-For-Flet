import flet
from flet import Container,Row,Column,Text, Page, colors,padding,margin,alignment,border,border_radius


list_name = ["John","Danai","Som","Sriwan","Tom"]


def DisplayNameAll():
    Text_name = []
    for i in list_name:
        Text_name.append(Text(i))

    return Column(
    Text_name,alignment="center",spacing=50
)


def Test_row():
    return Row(
        [Text("ทดสอบที่ 1"),Text("ทดสอบที่ 2"),Text("ทดสอบที่ 3"),Text("ทดสอบที่ 4")],alignment="center",spacing=50
    )


def main(page: Page):
    page.title = "แอพนะจ๊ะ"
    
    c1 = Container(
        content=DisplayNameAll()
    )
    page.add(c1)
    


flet.app("wk18k",target=main,view=flet.WEB_BROWSER,port=5000)
