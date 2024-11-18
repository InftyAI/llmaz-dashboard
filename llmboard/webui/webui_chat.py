import random

import gradio as gr

from llmboard.webui.engine import Engine

loaded = False


def create_chat_webui(engine: Engine) -> gr.Tab:
    def predict(message, history):
        print(f"message: {message}, history: {history}")
        return random.choice(["Yes", "No"])

    data = {
        "family1": ["model1", "model2", "model3"],
        "family2": ["model4", "model5"],
        "family3": ["model6", "model7", "model8", "model9"],
        "llama": ["model6", "model7", "model8", "llama2"],
    }

    services = {
        "llama2": ["service1", "service2", "service3", "service4"],
    }

    def get_models(family):
        models = data.get(family, [])
        return gr.update(choices=models, value=models[0] if models else None)

    def get_services(model):
        svcs = services.get(model, [])
        return gr.update(choices=svcs, value=svcs[0] if svcs[0] else None)

    with gr.Tab("Chat"):
        with gr.Row():
            family_dropdown = gr.Dropdown(
                label="Select Model Family", choices=list(data.keys()), value=None
            )
            model_dropdown = gr.Dropdown(
                label="Select Model", choices=[], value=None, interactive=True
            )
            service_dropdown = gr.Dropdown(
                label="Select Service", choices=[], value=None, interactive=True
            )

            family_dropdown.change(
                get_models, inputs=family_dropdown, outputs=model_dropdown
            )
            model_dropdown.change(
                get_services, inputs=model_dropdown, outputs=service_dropdown
            )

        with gr.Accordion("click for more parameters...", open=False):
            temperature = gr.Slider(0, 100, step=5, label="temperature")
            stream = gr.Checkbox(label="stream")

        gr.ChatInterface(
            fn=predict,
            additional_inputs=[
                gr.Textbox(placeholder="this is optional", label="System Prompt"),
            ],
            type="messages",
        )
