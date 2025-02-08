import gradio as gr

from llmchat.webui.engine import Engine
from llmchat.webui.serving import create_serving_service


def launch_webui() -> gr.Blocks:
    engine = Engine()

    with gr.Blocks(title="llmchat") as blocks:
        create_serving_service(engine)

    return blocks
