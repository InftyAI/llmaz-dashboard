import gradio as gr

from console.webui.engine import Engine


def create_prompt_webui(engine: Engine) -> gr.Tab:
    with gr.Tab("Prompt"):
        pass
