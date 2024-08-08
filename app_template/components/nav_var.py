import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", margin_right="20px"), href=url,
        
        color= "#fff"
    )


def navbar_user() -> rx.Component:
    return rx.box(
      
        rx.hstack(
            rx.hstack(
                rx.image(
                    src="/app_icon.png",
                    width="2.60em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    "ipo", size="7", weight="bold", color="#fff"
                ),
                align_items="center",
            ),
            rx.hstack(
                rx.hstack(
                    navbar_link("Admin", "/dashboard/admin"),
                    navbar_link("verbales", "/dashboard/verbales"),
                    navbar_link("rra", "/dashboard/rra"),
                    spacing="5",
                    margin_right="70px",                    
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("user"),
                            size="2",
                            radius="full",
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item("Settings"),
                        rx.menu.item("Earnings"),
                        rx.menu.separator(),
                         rx.menu.item(rx.link( "Log out", href="/")),
                    ),
                    justify="end",
                ),
            ),
            justify="between",
            align_items="center",
        ),
    
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("user"),
                            size="2",
                            radius="full",  
                        ),
                        
                    ),
                    rx.menu.content(
                        rx.menu.item("Settings"),
                        rx.menu.item("Earnings"),
                        rx.menu.separator(),
                        rx.menu.item("Log out"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        background="#535353",
        padding="20px",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        border_radius="10px 10px 0px 0px"
    )