"""# Purpose: Provide user interaction options for the Nuclear Explostions Heat Map.

from shiny import ui

def get_HEAT_MAP_inputs():
    return ui.panel_sidebar(
        ui.h2("Nuclear Explosions Heat Map Interactions"),
        ui.tags.hr(),
        ui.h4("Country Select (Can choose multiple)"),
        ui.input_checkbox("HEAT_MAP_USA", "USA", value=True),
        ui.input_checkbox("HEAT_MAP_USSR", "USSR", value=True),
        ui.input_checkbox("HEAT_MAP_FRANCE", "FRANCE", value=True),
        ui.input_checkbox("HEAT_MAP_UK", "UK", value=True),
        ui.input_checkbox("HEAT_MAP_USA", "CHINA", value=True),
        ui.input_checkbox("HEAT_MAP_PAKIS", "PAKIS", value=True),
        ui.input_checkbox("HEAT_MAP_INDIA", "INDIA", value=True),
        ui.tags.hr(),
        ui.input_slider(
            "HEAT_MAP_YEAR_RANGE",
            "Nuclear Explosions Year Range",
            min=1945,
            max=1998,
            value=[1945, 1998],
        ),
        ui.tags.hr(),
        ui.input_numeric("HEAT_MAP_MIN_EXPLOSION", "Minimum Explosion Yield (kilotons of TNT):", value=0.0),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )"""