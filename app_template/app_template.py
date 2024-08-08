import reflex as rx
from rxconfig import config
from .pages.auth.login import login_default


@rx.page(title="login")

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.center(
            login_default(),
            width="100%",
            height="100vh",
            display="flex",
            align_items="center",
            justify_content="center",
        )
        
    ),


app = rx.App()
app.add_page(index)


