from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui
import shiny.experimental as x
from modules.data import data_ui, data_server
from modules.basics import basics_ui, basics_server
from modules.models import models_ui, models_server

app_ui = x.ui.page_navbar(
    ui.nav("Data", data_ui("tab1")),
    ui.nav("Basics", basics_ui("tab2")),
    ui.nav("Models", models_ui("tab3")),
)


def server(input: Inputs, output: Outputs, session: Session):
    data_server("tab1")
    basics_server("tab2")
    models_server("tab3")


app = App(app_ui, server)
