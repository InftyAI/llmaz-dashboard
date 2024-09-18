# TODO: Using logging once ready
# import logging

import gradio as gr

from console.webui.engine import Engine
from console.webui.webui_serving import create_serving_webui
from console.webui.webui_finetune import create_finetune_webui
from console.webui.webui_prompt import create_prompt_webui


def launch_webui() -> gr.Blocks:
    engine = Engine()

    with gr.Blocks(title="Console") as blocks:
        #  Serving Tab
        create_serving_webui(engine)
        #  Prompt Tab
        create_prompt_webui(engine)
        #  Fine-tuning Tab
        create_finetune_webui(engine)

    return blocks
