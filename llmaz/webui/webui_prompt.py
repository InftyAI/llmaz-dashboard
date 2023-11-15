import gradio as gr

from llmaz.webui.engine import Engine


def create_prompt_webui(engine: Engine) -> gr.Tab:
    with gr.Tab("Prompt"):
        pass
