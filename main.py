from flet import *

def main(page:Page):
	page.appbar = AppBar(title=Text("Yooutube app"))
	page.add(
		Container(
			bgcolor="red",
			padding=10,
			alignment=alignment.center,
			content=Text("hello",size=30,weight="bold")
			)
		)
app(main)
