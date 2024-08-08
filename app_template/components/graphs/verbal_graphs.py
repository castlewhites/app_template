import reflex as rx

data01 = [
    {"name": "pediente de gestión", "value": 400},
    {"name": "Nulo", "value": 300},
    {"name": "Pendiente doc", "value": 300},
    {"name": "Traslado a SSPD", "value": 200},
  
]

def pie_simple():
    return rx.recharts.pie_chart(
        rx.recharts.pie(
            data=data01,
            data_key="value",
            name_key="name",
            fill="#8884d8",
            label=True,
            
        ),
        rx.recharts.graphing_tooltip(),
        width="100%",
        height=300,
    )