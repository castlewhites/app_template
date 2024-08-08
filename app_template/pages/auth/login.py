import reflex as rx



def login_default() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/app_icon.png",
                    width="4.5em",
                    height="auto",
                   
                ),
                rx.heading(
                    "ipo",
                    size="8",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Usuario",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="Ingresar email",
                    type="email",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Contraseña",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "Recuperar contraseña",
                        href="/remember_password",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    placeholder="Ingresar contraseña",
                    type="password",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Ingresar", size="3", width="100%", background_color= "#284068", border= "1px solid #284068", on_click= rx.redirect("/dashboard/admin")),
            rx.center(
                rx.link("Crear nuevo usuario", href="#", size="3"),
                opacity="0.8",
                width= "100%",
                display= "flex",
                justify= "center"
              
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="23em",
        width="100%",
        box_shadow="0 4px 8px 0 rgba(0, 0, 0, 0.2)",
    )