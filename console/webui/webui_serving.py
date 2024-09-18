import gradio as gr
from llmlite.apis import ChatMessage

from console.webui.engine import Engine


loaded = False


def create_serving_webui(engine: Engine) -> gr.Tab:
    def predict(message, history, system_prompt):
        messages = []
        for i in range(0, len(history)):
            messages.append(ChatMessage(role="user", content=history[i][0]))
            messages.append(ChatMessage(role="assistant", content=history[i][1]))

        messages.append(ChatMessage(role="user", content=message))

        # TODO: https://github.com/InftyAI/llmlite/issues/31
        if system_prompt != "":
            messages = [ChatMessage(role="system", content=system_prompt)] + messages

        return engine.serve.completion(messages=messages)

    with gr.Tab("Serving"):
        with gr.Row():
            # TODO: required validation, see https://github.com/gradio-app/gradio/issues/2718
            model_name = gr.Textbox(
                label="model_name_or_path",
                placeholder="this is required",
            )
            task = gr.Textbox(
                label="task",
                placeholder="this is optional, default to text-generation",
            )

        with gr.Accordion("click for more parameters...", open=False):
            temperature = gr.Slider(0, 100, step=5, label="temperature")
            stream = gr.Checkbox(label="stream")

        with gr.Row():
            load_btn = gr.Button("Load Model", interactive=(not loaded))
            offload_btn = gr.Button("Offload Model", interactive=loaded)

            # TODO: https://github.com/InftyAI/Llmaz/issues/6
            load_btn.click(
                fn=engine.preload_model,
                inputs=[model_name, task, temperature, stream],
            ).success(
                lambda b: gr.update(interactive=False),
                inputs=[load_btn],
                outputs=[load_btn],
            ).success(
                lambda b: gr.update(interactive=True),
                inputs=[offload_btn],
                outputs=[offload_btn],
            )
            offload_btn.click(
                fn=engine.offload_model,
            ).success(
                lambda b: gr.update(interactive=False),
                inputs=[offload_btn],
                outputs=[offload_btn],
            ).success(
                lambda b: gr.update(interactive=True),
                inputs=[load_btn],
                outputs=[load_btn],
            )

        with gr.Tab("Chatbot"):
            gr.ChatInterface(
                predict,
                retry_btn=None,
                undo_btn=None,
                additional_inputs=[
                    gr.Textbox(placeholder="this is optional", label="system prompt"),
                ],
            )

        # TODO: Just for demonstration, once we have another application for serving, remove it.
        with gr.Tab("PR-Copilot"):
            pass
        with gr.Tab("RAG"):
            pass
