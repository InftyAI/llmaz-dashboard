import gradio as gr

from llmchat.webui.engine import Engine
from llmchat.webui.webui_serving import create_serving_webui


def launch_webui() -> gr.Blocks:
    engine = Engine()

    with gr.Blocks(title="llmchat") as blocks:
        #  Serving Tab
        create_serving_webui(engine)

    return blocks
