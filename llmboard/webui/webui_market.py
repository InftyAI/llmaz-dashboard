import gradio as gr
import requests

from llmboard.webui.engine import Engine


def fetch_readme(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Load document error"


def create_market_webui(engine: Engine) -> gr.Tab:
    with gr.Tab("Model Market"):
        with gr.Row():
            with gr.Group():
                gr.Markdown("## Model Card1")

            with gr.Group():
                gr.Markdown("## Model Card2")

            with gr.Group():
                gr.Markdown("## Model Card3")

        with gr.Row():
            with gr.Group():
                gr.Markdown("## Model Card4")

            with gr.Group():
                gr.Markdown("## Model Card5")

            with gr.Group():
                gr.Markdown("## Model Card6")
