import reflex as rx

data = [
    {"name": "Analista", "uv": 4000, },
    {"name": "Admin", "uv": 3000, },
]


def bar_simple():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="uv",
            stroke= "#284068",
            fill="#284068",
        ),
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.graphing_tooltip(),
        data=data,
        width="100%",
        height=250,
        bar_size=80,
    )