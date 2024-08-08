import reflex as rx
from ..components.nav_var import navbar_user
from ..components.modules_wrapper.stats_section.admin_stats import admin_stats
from ..components.modules_wrapper.table_section.admin_table import table


@rx.page(route="/dashboard/admin", title="ipo")

def admin_page() -> rx.Component:
    return rx.vstack(
        navbar_user(),
        admin_stats(),
        table(),

       
        width="100%", 
        display="flex",
        justify_content="center",
        max_width="70%", 
        margin="0 auto", 
        border_radius="10px",
        border="1px solid grey",
        box_shadow="0 4px 8px 0 rgba(0, 0, 0, 0.2)",      
       
    )