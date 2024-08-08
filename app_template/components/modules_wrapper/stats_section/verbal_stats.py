import reflex as rx
from ...graphs.admin_graphs import bar_simple
from ...graphs.verbal_graphs import pie_simple

def verbal_stats() -> rx.Component:
    # Valores inventados para el ejemplo
    data = {
        "user_counts": {
            "Total usuarios": 14,
            "Usuarios conectados": 0,
            "Usuarios por validar": 3,
            "Usuarios inactivos": 0
        }
    }
    
    

    
    
    # Crear el componente
    return rx.vstack(
        rx.section(
            rx.heading("Administración de usuarios", width="100%", text_align="center", color="#535353"), 
            border_bottom="1px solid gray",
            width="100%",
            height="45px",
            padding="0px"
        ),
        rx.hstack(
            rx.flex(
               rx.box(   
                    rx.vstack(
                        rx.text("4.833", font_size="70px", color="#535353"),
                        rx.text("Total PQRs", size="4", color="#666", margin_right="6px", text_align="center"),
                        spacing="20px", 
                        align_items="center"
                    ),
                       
          
                    display="flex",
                    
                    padding="10px",
                    border_radius="8px",
                    justify_content="space-around",
                ),
                rx.box(
                    pie_simple(),
                    width="25%"
                ),
                rx.box(
                    bar_simple(),
                    width="48%",  
                    padding="10px",    
                    border_radius="8px"
                ),
                width="100%",
                height="100%",
                spacing="2",
                justify_content="space-between",  
                align_items="center" 
            ),
            width="90%",
            margin="0 auto"
        ),
        width="100%",
        margin_top="10px",
        margin="0 auto",
        padding="10px"
    )
