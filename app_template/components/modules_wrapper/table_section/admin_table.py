import pandas as pd
import reflex as rx

# Datos de ejemplo
data = {
    "Nombre": ["Juan Perez", "Ana Gómez", "Luis Martínez"],
    "Correo": ["juan@example.com", "ana@example.com", "luis@example.com"],
    "Telefono": ["123-456-7890", "234-567-8901", "345-678-9012"],
    "Dirección": ["Calle 123", "Avenida 45", "Boulevard 678"],
    "Fecha inicio": ["2024-01-01", "2024-02-01", "2024-03-01"],
    "Estado": ["Activo", "Inactivo", "Activo"]
}

df = pd.DataFrame(data)


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
            color="#fff"
        ),
    )

def _table_cell(text: str):
    return rx.table.cell(rx.text(text))




def table():
    return rx.fragment(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Nombre", "user"),
                    _header_cell("Correo", "mail"),
                    _header_cell("Telefono", "phone"),
                    _header_cell("Dirección", "home"),
                    _header_cell("Fecha inicio", "calendar"),
                    _header_cell("Estado", "truck"),
                ),
                
                background="#535353",
                
            ),
            rx.table.body(
                *[
                    rx.table.row(
                        _table_cell(row["Nombre"]),
                        _table_cell(row["Correo"]),
                        _table_cell(row["Telefono"]),
                        _table_cell(row["Dirección"]),
                        _table_cell(row["Fecha inicio"]),
                        _table_cell(row["Estado"]),
                    )
                    for index, row in df.iterrows()
                ]
            ),
            
            variant="surface",
            size="3",
            width="90%",
            margin="0 auto"
      
        ),
    )