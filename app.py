from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui, module
import shiny.experimental as x
from modules.data import data_ui, data_server
from modules.basics import basics_ui, basics_server
from modules.models import models_ui, models_server
from starlette.routing import Mount
from starlette.applications import Starlette


# Defining the ui as a function allows us to pass a selected tab argument to it
# this will be used in routing.
def top_ui(selected):
    return x.ui.page_navbar(
        ui.nav("Data", data_ui("tab1")),
        ui.nav("Basics", basics_ui("tab2")),
        ui.nav("Models", models_ui("tab3")),
        selected=selected,
    )


def top_server(input: Inputs, output: Outputs, session: Session):
    data_server("tab1")
    basics_server("tab2")
    models_server("tab3")


def mount_tab(tab):
    return Mount(
        f"/{tab.lower()}",
        App(top_ui(selected=tab), top_server),
    )


# Define routes for the application
tabs = ["Data", "Basics", "Models"]
routes = [mount_tab(tab) for tab in tabs]
routes.append(Mount("/", App(top_ui(selected="Data"), top_server)))

# We call the Sarlette function directly so that we can pass in the route
# information.
app = Starlette(routes=routes)
