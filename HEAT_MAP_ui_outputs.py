"""# Purpose: Display output for Nuclear Explosions Heat Map.

from shiny import ui
from shinywidgets import output_widget


def get_HEAT_MAP_outputs():
    return ui.panel_main(
        ui.h2("Nuclear Explosions World Heat Map"),
        ui.tags.hr(),
        ui.tags.section(
            output_widget("HEAT_MAP_output_widget1"),
            ui.tags.hr(),
            ui.h3("Filtered Nuclear Explosions World Heat Map Table"),
            ui.output_text("HEAT_MAP_record_count_string"),
            ui.output_table("HEAT_MAP_filtered_table"),
            ui.tags.hr(),
        ),
    )"""