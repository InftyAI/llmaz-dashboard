# TODO: Using logging once ready
# import logging

import gradio as gr

from llmaz.webui.engine import Engine
from llmaz.webui.webui_serving import create_serving_webui


def launch_webui() -> gr.Blocks:
    engine = Engine()

    with gr.Blocks(title="Llmaz") as blocks:
        #  Serving Tab
        create_serving_webui(engine)

    return blocks
