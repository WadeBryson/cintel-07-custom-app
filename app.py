"""
Purpose: Use Python to create a continuous intelligence and 
interactive analytics dashboard using Shiny for Python.

Each Shiny app has two parts: 

- a user interface app_ui object (similar to the HTML in a web page) 
- a server function that provides the logic for the app (similar to JS in a web page).

"""
import shinyswatch
from shiny import App, ui, render

#TODO Fix these
from NE_DATA_server import get_NE_DATA_server_functions
from NE_DATA_ui_inputs import get_NE_DATA_inputs
from NE_DATA_ui_outputs import get_NE_DATA_outputs

# from HEAT_MAP_server import get_COLD_WAR_server_functions
# from HEAT_MAP_ui_inputs import get_COLD_WAR_inputs
# from HEAT_MAP_ui_outputs import get_COLD_WAR_outputs

from util_logger import setup_logger

logger, logname = setup_logger(__name__)

app_ui = ui.page_navbar(
    shinyswatch.theme.darkly(),
    ui.nav(
        "Home",
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.h2("Project 7 - Custom Reactive App"),
                ui.tags.hr(),
                ui.h3("Author - Wade Bryson"),
                ui.h4("Class - 44630 Continuous Intelligence and Interactive Analytics"),
                ui.h4("Summer 2023 OP Block 2")
                ),
                ui.tags.hr(),
            ),
            ui.panel_main(
                ui.h2("Nuclear Explosions Interactive Data"),
                ui.tags.hr(),
                ui.tags.ul(
                    ui.tags.li(
                        "To explore Nuclear Explosions dataset, click the 'NE_Data' tab."
                    ),
                    ui.tags.li(
                        "To explore the USA vs USSR dataset, click the 'Cold_War' tab."
                    ),
                ),
                ui.tags.hr(),
                ui.h3("Inspiration"),
                ui.tags.hr(),
                ui.h4("This project was inspired from watching the recent hit movie Oppenheimer"),
                ui.tags.hr(),
            ),
        ),
    ),
ui.nav(
        "NE_Data",
        ui.layout_sidebar(
            get_NE_DATA_inputs(),
            get_NE_DATA_outputs(),
        ),
    ),
#TODO Fix
"""ui.nav(
        "Cold_War",
        ui.layout_sidebar(
            #TODO Fix
            get_COLD_WAR_inputs(),
            get_COLD_WAR_outputs(),
        ),
    ),"""
ui.nav(ui.a("About", href="https://github.com/WadeBryson")),
ui.nav(ui.a("GitHub", href="https://github.com/WadeBryson/cintel-07-custom-app")),
ui.nav(ui.a("App", href="https://wadebryson.shinyapps.io/cintel-07-custom-app/")),
title=ui.h1("Wade Bryson Dashboard"),

def server(input, output, session):
    """Define functions to create UI outputs."""

    logger.info("Starting server...")
    get_NE_DATA_server_functions(input, output, session)
    # get_HEAT_MAP_server_functions(input, output, session)

# app = App(app_ui, server, debug=True)
app = App(app_ui, server)