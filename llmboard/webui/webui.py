import gradio as gr

from llmboard.webui.engine import Engine
from llmboard.webui.webui_chat import create_chat_webui
from llmboard.webui.webui_market import create_market_webui


def launch_webui() -> gr.Blocks:
    engine = Engine()

    with gr.Blocks(title="llmboard") as blocks:
        #  TODO: Model Market Tab, list and create serving services.
        # create_market_webui(engine)
        #  Serving Tab
        create_chat_webui(engine)

    return blocks
