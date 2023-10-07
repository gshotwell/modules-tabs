from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui, module


@module.ui
def data_ui():
    return ui.page_fluid(
        ui.h1("Some Data!"),
        ui.input_slider("n", "N", 0, 100, 20),
        ui.output_text_verbatim("txt"),
    )


@module.server
def data_server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"
