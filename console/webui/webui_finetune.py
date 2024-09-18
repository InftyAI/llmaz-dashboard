import gradio as gr

from console.webui.engine import Engine


def create_finetune_webui(engine: Engine) -> gr.Tab:
    with gr.Tab("Fine-Tuning"):
        pass
