import gradio as gr

from llmchat.webui.engine import Engine


loaded = False


def create_serving_webui(engine: Engine) -> gr.Tab:
    def predict(message, history, system_prompt):
        return f"message: {message}, history: {history}, system_prompt: {system_prompt}"

    with gr.Tab("Serving"):
        with gr.Row():
            # TODO: required validation, see https://github.com/gradio-app/gradio/issues/2718
            model_name = gr.Textbox(
                label="model_name_or_path",
                placeholder="this is required",
            )

        with gr.Accordion("click for more parameters...", open=False):
            temperature = gr.Slider(0, 2, step=0.1, label="temperature")
            stream = gr.Checkbox(label="stream")

        with gr.Tab("Chatbot"):
            gr.ChatInterface(
                predict,
                retry_btn=None,
                undo_btn=None,
                additional_inputs=[
                    gr.Textbox(placeholder="this is optional", label="system prompt"),
                ],
            )
