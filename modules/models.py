from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui, module


@module.ui
def models_ui():
    return ui.page_fluid(
        ui.h1("Some Models!"),
        ui.input_slider("n", "N", 0, 100, 20),
        ui.output_text_verbatim("txt"),
    )


@module.server
def models_server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"
